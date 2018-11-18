#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>

#define STDIN 0
#define BUFFSIZE 1000000

int sockfd;

void signal_callback_handler(int signum)
{
	close(sockfd);
	exit(signum);
}

int main(int argc, char *argv[])
{
	
	signal(SIGINT, signal_callback_handler);

	struct addrinfo hints, *result, *iterator;

	if(argc < 2 || argc > 3) {
		fprintf(stderr, "Usage %s <hostname> [<port>]\n", argv[1]);
		return 2;
	}

	char portno[10];
	if(argc == 2) {
		strcpy(portno, "23");
	}
	else {
		strcpy(portno, argv[2]);
	}

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;

	int hostresolution = getaddrinfo(argv[1], portno, &hints, &result);
	if(hostresolution != 0) {
		fprintf(stderr, "Error in host resolution: %s\n", gai_strerror(hostresolution));
		return 2;
	}

	struct sockaddr_in *ip_Addr;

	for(iterator = result; iterator; iterator=iterator->ai_next)
	{
		sockfd = socket(iterator->ai_family, iterator->ai_socktype, 0);

		if(sockfd == -1)
			continue;

		ip_Addr = (struct sockaddr_in*)iterator->ai_addr;

		if(connect(sockfd, (struct sockaddr *)ip_Addr, iterator->ai_addrlen) != -1) {
			break;	
		}

		close(sockfd);
	}

	freeaddrinfo(result);

	if(iterator == NULL) {
		fprintf(stderr, "%s\n", "Could not connect! Connection timed out.");
		return 2;
	}

	unsigned char s[INET_ADDRSTRLEN];
	inet_ntop(AF_INET, &(ip_Addr->sin_addr), s, INET_ADDRSTRLEN);
	printf("Connected to %s\n", s);

	fd_set inputfd;
	unsigned char serverInput[BUFFSIZE];
	char serverOutput[BUFFSIZE];
	char *userInput = NULL;

	for(;;) {

		FD_ZERO(&inputfd);
		FD_SET(STDIN, &inputfd);
		FD_SET(sockfd, &inputfd);

		int check = select(sockfd + 1, &inputfd, NULL, NULL, NULL);
		if(check < 0) {
			fprintf(stderr, "%s\n", "Problem in I/O multiplexing.");
			return 2;
		}

		if(FD_ISSET(sockfd, &inputfd)) {
			memset(&serverInput, 0, sizeof(serverInput));
			ssize_t serverRead = recv(sockfd, serverInput, BUFFSIZE - 1, 0);
			if(serverRead < 0) {
				fprintf(stderr, "%s\n", "Could not read from server");
				continue;
			}else if(serverRead == 0) {
				fprintf(stderr, "%s\n", "No more data, exiting");
				return 2;	
			}

			memset(&serverOutput, 0, sizeof(serverOutput));
			int i = 0, j = 0;
			serverInput[serverRead] = '\0';
			int flag = 0;
			while(serverInput[i]) {
				if(serverInput[i] == 255) {
					serverOutput[j] = 255; j++; i++;
					switch(serverInput[i]) {
						case 251 : serverOutput[j] = 254; j++; i++; break;
						case 253 : serverOutput[j] = 252; j++; i++; break;
						case 254 : 
						case 252 : j--; i++; i++; flag  = 1; break;
					}
					if(!flag)
					{
						serverOutput[j] = serverInput[i];
						i++; j++;
					}
				}
				else {
					printf("%c", serverInput[i]);
					i++;
					fflush(stdout);
				}
			}
			if(j > 0) {
				serverOutput[j] = '\0';
				if(flag){
					serverOutput[0] = '\0';
					j = 0;
				}			
				int check = send(sockfd, serverOutput, j, 0);
				if(check == -1) {
					fprintf(stderr, "%s\n", "Could not send data to server.");
				}
			}
		}
		if(FD_ISSET(STDIN, &inputfd)) {
			ssize_t len = 0;
			int n = getline(&userInput, &len, stdin);
			userInput[n - 1] = '\r';
			userInput[n] = '\n';
			userInput[n + 1] = '\0';
			send(sockfd, userInput, n + 1, 0);
		}

	}

	return 0;
}