package translib

import (
	"fmt"
        "github.com/sbinet/go-python"
)

func translate(db_id int, json string) {

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
        python.PyTuple_SetItem(_args, 0, python.PyInt_FromLong(db_id))
        python.PyTuple_SetItem(_args, 1, python.PyString_FromString(json))

        result := translateFunc.Call(_args, python.PyDict_New())
        fmt.Println(python.PyDict_Check(result))

        var key *python.PyObject
        var value *python.PyObject
        var pos int

        for python.PyDict_Next(result, &pos, &key, &value) {
                fmt.Println(python.PyString_AsString(key))
                if python.PyDict_Check(value) {
                        var _key *python.PyObject
                        var _value *python.PyObject
                        var _pos int
                        for python.PyDict_Next(value, &_pos, &_key, &_value) {
                                fmt.Println(python.PyString_AsString(_key))
                        	// get key and data
                        	if python.PyDict_Check(_value) {
                        		var __key *python.PyObject
                        		var __value *python.PyObject
                        		var __pos int

                        		for python.PyDict_Next(_value, &__pos, &__key, &__value) {
                                		fmt.Println(python.PyString_AsString(__key), "=", python.PyString_AsString(__value))
                        		}
                        	}
                        }
                } else {
                        fmt.Println(python.PyString_AsString(value))
                }
        }

	return
}

