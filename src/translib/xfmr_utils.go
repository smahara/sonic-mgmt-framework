package translib

import (
	"fmt"
	"errors"
	"translib/db"
	"github.com/sbinet/go-python"
)

// TODO - Py-DECREF, GIL, Initialize/finalize with optimization
func translate_to_db(d *db.DB, json []byte) (map[string]map[string]db.Value, error) {
	var err error
	// table.key.fields
	var result = make(map[string]map[string]db.Value)
	
	python.Initialize()
	defer python.Finalize()

	transformerModule := python.PyImport_ImportModule("transformer")
	if transformerModule == nil {
		panic("Error importing module")
	}

	translateFunc := transformerModule.GetAttrString("translate")
	if translateFunc == nil {
		panic("Error importing function")
	}

	_args := python.PyTuple_New(2)
	python.PyTuple_SetItem(_args, 0, python.PyInt_FromLong(int(d.Opts.DBNo)))
	python.PyTuple_SetItem(_args, 1, python.PyString_FromString(string(json)))

	obj := translateFunc.Call(_args, python.PyDict_New())
	//fmt.Println(python.PyDict_Check(obj))
	if obj == nil {
		return nil, errors.New("failed to translate")
	}

	//var db_table, db_key, db_field, db_value []byte
	var key *python.PyObject
	var value *python.PyObject
	var pos int

	for python.PyDict_Next(obj, &pos, &key, &value) {

		db_table := make([]byte, len(python.PyString_AsString(key)))
		copy(db_table, python.PyString_AsString(key))
		result[string(db_table)] = make(map[string]db.Value)
				
		if python.PyDict_Check(value) {
			var _key *python.PyObject
			var _value *python.PyObject
			var _pos int

			for python.PyDict_Next(value, &_pos, &_key, &_value) {
	
				db_key := make([]byte, len(python.PyString_AsString(_key)))
				copy(db_key, python.PyString_AsString(_key))
				
				// get key and data
				if python.PyDict_Check(_value) {
					var __key *python.PyObject
					var __value *python.PyObject
					var __pos int
			
					field := make(map[string]string)
					result[string(db_table)][string(db_key)] = db.Value{Field: field}
								
					for python.PyDict_Next(_value, &__pos, &__key, &__value) {
						db_field := make([]byte, len(python.PyString_AsString(__key)))
						copy(db_field, python.PyString_AsString(__key))
						
						db_value := make([]byte, len(python.PyString_AsString(__value)))
						copy(db_value, python.PyString_AsString(__value)) 
						result[string(db_table)][string(db_key)].Field[string(db_field)] = string(db_value)
					}
				}
			}
		} else {
			fmt.Println(python.PyString_AsString(value))
		}
	}

	return result, err
}

