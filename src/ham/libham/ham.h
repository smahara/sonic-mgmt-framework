// Host Account Management
#ifndef __HAM_LIB_H
#define __HAM_LIB_H

#include <stdbool.h>    /* bool */
#include <grp.h>        /* gid_t, struct group */
#include <pwd.h>        /* uid_t, struct passwd */

#ifdef __cplusplus
extern "C" {
#endif

int ham_useradd(const char * login, const char * options);
int ham_usermod(const char * login, const char * options);
int ham_groupadd(const char * group, const char * options);
int ham_groupmod(const char * group, const char * options);

#ifdef __cplusplus
}
#endif

#endif // __HAM_LIB_H

