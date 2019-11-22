// Host Account Management
#ifndef __UTILS_H
#define __UTILS_H

#include <string.h>             /* strcmp(), strncmp() */
#include <systemd/sd-journal.h> /* sd_journal_print() */

#define LOG_CONDITIONAL(condition, args...) do { if (condition) {sd_journal_print(args);} } while(0)

#define streq(a,b)    (strcmp((a),(b)) == 0)
#define strneq(a,b,n) (strncmp((a),(b),(n)) == 0)

/**
 * @brief Checks that a string starts with a given prefix.
 *
 * @param s The string to check
 * @param prefix A string that s could be starting with
 *
 * @return If s starts with prefix then return a pointer inside s right
 *         after the end of prefix.
 *         NULL otherwise
 */
static inline char * startswith(const char *s, const char *prefix)
{
    size_t l = strlen(prefix);
    if (strncmp(s, prefix, l) == 0) return (char *)s + l;

    return NULL;
}

/**
 * Copy string to buffer
 *
 * @param dest Where to copy srce to
 * @param srce String to be copied
 * @param len  Number of characters to copy.
 *
 * @return a pointer to the location in dest after the NUL terminating
 *         character of the string that was copied.
 */
static inline char * cpy2buf(char * dest, const char * srce, size_t len)
{
    memcpy(dest, srce, len);
    return dest + len;
}




#ifdef __cplusplus
#   include <string>
#   include <sstream>               /* std::ostringstream */

    inline const char * true_false(bool x, const char * pos_p = "true", const char * neg_p = "false")   { return (x) ? pos_p : neg_p; }

    /**
     * This is an equivalent to Python's ''.join().
     *
     * @example
     *
     *      static std::vector<std::string> v = {"a", "b", "c"};
     *      std::string s = join(v.begin(), v.end(), ", ", ".");
     *      // Result: "a, b, c."
     *
     * @return std::string
     */
    template<typename InputIt>
    std::string join(InputIt begin,
                     InputIt end,
                     const std::string & separator =", ",
                     const std::string & concluder ="")
    {
        std::ostringstream ss;

        if (begin != end)
        {
            ss << *begin++;
        }

        while (begin != end)
        {
            ss << separator;
            ss << *begin++;
        }

        ss << concluder;
        return ss.str();
    }
#endif // __cplusplus

#endif /* __UTILS_H */
