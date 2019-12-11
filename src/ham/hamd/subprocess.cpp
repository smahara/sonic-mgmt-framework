#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/socket.h>         // recv(), MSG_DONTWAIT
#include <limits.h>             // LINE_MAX
#include <string>               // std::string
#include <tuple>                // std::tuple

#include "subprocess.h"         // run()

#define SHELL_PATH  "/bin/sh"
#define SHELL_NAME  "sh"

class StdPipe
{
private:
    int   stdfd_m = -1;
    int   fds[2];
    bool  failure = false;

    void _close(int id)
    {
        if (fds[id] != -1)
        {
            ::close(fds[id]);
            fds[id] = -1;
        }
    }

    int _dup(int id)
    {
        if (fds[id] == -1) return -1;
        int new_fd = ::dup2(fds[id], stdfd_m);
        _close(id);
        return new_fd;
    }

public:
    StdPipe(int stdfd) :stdfd_m(stdfd)
    {
        fds[0] = -1; // Reader
        fds[1] = -1; // Writer
        failure = 0 == ::pipe(fds);
    }

    ~StdPipe()
    {
        close();
    }

    bool failed() const { return failure; }

    int  remap_rd() { return _dup(0); }
    int  remap_wr() { return _dup(1); }

    void close_rd() { _close(0); }
    void close_wr() { _close(1); }
    void close()    { _close(0); _close(1); }

    std::string get()
    {
        if (failure)
            return "failed to create pipe";

        if (fds[0] != -1)
        {
            char buf[LINE_MAX];
            if (::recv(fds[0], buf, sizeof(buf), MSG_DONTWAIT) > 0)
                    return buf;
        }

        return "";
    }
};

std::tuple<int/*rc*/, std::string/*stdout*/, std::string/*stderr*/> run(const std::string & cmd_r)
{
    StdPipe  std_out(STDOUT_FILENO);
    StdPipe  std_err(STDERR_FILENO);

    if (std_out.failed() || std_err.failed())
        return std::make_tuple(-1, "", "failed to create pipe");

    pid_t  pid = fork();

    if (pid < (pid_t)0) // Did fork fail?
        return std::make_tuple(-1, "", "failed to fork process");

    if (pid == (pid_t)0) /* Child */
    {
        std_out.close_rd(); // close the read end of the pipe in the child
        std_err.close_rd(); // close the read end of the pipe in the child

        std_out.remap_wr(); // Map writer end of pipe to child's stdout
        std_err.remap_wr(); // Map writer end of pipe to child's stderr

        const char  * new_argv[4];
        new_argv[0] = SHELL_NAME;
        new_argv[1] = "-c";
        new_argv[2] = cmd_r.c_str();
        new_argv[3] = NULL;

        /* Exec the shell.  */
        (void)execve(SHELL_PATH, (char *const *)new_argv, environ);

        exit(127); // exit the child
    }

    /* Parent */
    std_out.close_wr(); // close the write end of the pipe in the parent
    std_err.close_wr(); // close the write end of the pipe in the parent

    int exit_status = -1;
    if (TEMP_FAILURE_RETRY(waitpid(pid, &exit_status, 0)) != pid)
        exit_status = -1;

    bool term_normal = WIFEXITED(exit_status);
    if (!term_normal)
        return std::make_tuple(-1, "", "abnormal command termination");

    int    rc = WEXITSTATUS(exit_status);
    return std::make_tuple(rc, std_out.get(), std_err.get());
}
