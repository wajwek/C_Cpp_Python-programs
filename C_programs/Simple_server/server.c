#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>
#include <signal.h>

#define PORT 8080

//=================================MAIN=============================================


int main(void) {
    
    signal(SIGCHLD, SIG_IGN); // We are deleting zombie processes

    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) {
        perror("socket");
        return 1;
    }

    int yes = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(server_fd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("bind");
        close(server_fd);
        return 1;
    }

    if (listen(server_fd, 10) < 0) {
        perror("listen");
        close(server_fd);
        return 1;
    }

    printf("Listening on http://localhost:%d/\n", PORT);
    int counter = 1;
    for (;;) {
        int client_fd = accept(server_fd, NULL, NULL);
        char client_fd_str[12];
        char counter_str[12];
        sprintf(counter_str, "%d", counter);
        sprintf(client_fd_str, "%d", client_fd);
        if (client_fd < 0) {
            perror("accept");
            continue;
        }

        int child;
        if ((child = fork()) == 0){
            close(server_fd);
            execl("client-service", "client-service", client_fd_str, counter_str, NULL);   
        }
        counter += 1;
        close(client_fd);
    }
    close(server_fd);
    return 0;
}