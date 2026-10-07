#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

void handle_client(int client_fd, int counter) {

    char buf[1024];
    read(client_fd, buf, sizeof(buf));

    FILE *file = fopen("site.html", "rb");
    if (!file) {
        perror("fopen(site.html)");
        close(client_fd);
        return;
    }
    const char *header =
        "HTTP/1.0 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "\r\n";

    if(send(client_fd, header, strlen(header), MSG_NOSIGNAL) <= 0) {
        fclose(file);
        close(client_fd);
        return;
    }

    size_t n;
    while ((n = fread(buf, 1, sizeof(buf), file)) > 0) {
        size_t off = 0;
        while (off < n) {
            ssize_t sent = send(client_fd, buf + off, n - off, MSG_NOSIGNAL);
            if(sent <= 0) {
                fclose(file);
                close(client_fd);
                return;
            }
            off += sent;
        }
    }

    printf("Connection no. %d finished\n", counter);
    fclose(file);
    close(client_fd);
}

int main(int argc, char *argv[]) {
    int client_fd;
    client_fd = atoi(argv[1]);
    int counter;
    counter = atoi(argv[2]);
    handle_client(client_fd, counter);
    exit(0);
}
