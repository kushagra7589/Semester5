#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>

unsigned char negotiate(unsigned char command) {
	switch(command) {
		case 251 : return 254;
		case 253 : return 252;
	}
}

int main(int argc, char *argv[]) 
{

	int sockfd;

	if(argc < 2 || argc > 3) 
	{
		fprintf(stderr, "Usage %s <hostname> [<port>]\n", argv[0]);
		return 2;
	}

	struct addrinfo *res, hints, *p;

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;

	unsigned char port[10];
	if(argc == 3){
		strcpy(port, argv[2]);
	}
	else {
		strcpy(port, "23");
	}
	int hostresolution = getaddrinfo(argv[1], port, &hints, &res);
	if(hostresolution != 0) 
	{
		fprintf(stderr, "Error at getaddrinfo: %s\n", gai_strerror(hostresolution));
		return 2;
	}

	struct sockaddr_in *ip_Addr;

	for(p = res; p != NULL; p = p->ai_next) 
	{
		sockfd = socket(p->ai_family, p->ai_socktype, 0);

		if(sockfd == -1)
		{
			continue;	// try to create a socket at next address
		}
		ip_Addr = (struct sockaddr_in*)p->ai_addr;
		char s[INET_ADDRSTRLEN];
		inet_ntop(AF_INET, &(ip_Addr->sin_addr), s, INET_ADDRSTRLEN);
		printf("Trying %s...\n", s);
		if(connect(sockfd, (struct sockaddr *)ip_Addr, p->ai_addrlen) != -1) {
			break;	
		}

		close(sockfd);
	}

	if(p == NULL) 
	{
		fprintf(stderr, "Could not connect!\n");
		return 2;
	}

	unsigned char s[INET_ADDRSTRLEN];
	inet_ntop(AF_INET, &(ip_Addr->sin_addr), s, INET_ADDRSTRLEN);
	printf("Connected to %s\n", s);
	fflush(stdout);
	freeaddrinfo(res);


	
	int DATASIZE = 1e5 + 1;
	unsigned char inputBuffer[DATASIZE];
	unsigned char outputBuffer[DATASIZE];
	unsigned char readInput[DATASIZE];

	struct timeval tv;
	tv.tv_sec = 10;
	tv.tv_usec = 50000;

	for(;;)
	{
		fd_set readfds;
		FD_ZERO(&readfds);
		FD_SET(sockfd, &readfds);
		FD_SET(0, &readfds);
		fprintf(stderr, "%s\n", "Select se pehle");
		int ret = select(sockfd + 1, &readfds, NULL, NULL, NULL	);
		fprintf(stderr, "%d\n", ret);
		if(ret <= 0) {
			fprintf(stderr, "Select not working\n");
			return 2;
		}
		fprintf(stderr, "%s\n", "select ke baad");
		int outputIndex;
		if(FD_ISSET(sockfd, &readfds))
		{
			fprintf(stderr, "%s\n", "Server is sending data");
			outputIndex = 0;
			ssize_t nread;
			nread = recv(sockfd, inputBuffer, (int)1e4, 0);
			// fprintf(stderr, "%s\n", );
			printf("Bytes Received: %d\n", (int)nread);
			if(nread == -1) {
				fprintf(stderr, "%s\n", "Could not read data server");
			}
			else {
				// inputBuffer[nread] = '\0';
				for(int i = 0; i < nread; i++) {
					if(inputBuffer[i] == 255) {
						fprintf(stderr, "%s\n", "Found IAC");
						outputBuffer[outputIndex++] = 255;
						i++;
						if(inputBuffer[i] == 251 || inputBuffer[i] == 253) {
							outputBuffer[outputIndex++] = negotiate(inputBuffer[i]);i++;
							outputBuffer[outputIndex++] = inputBuffer[i];
						}
						else if(inputBuffer[i] == 252 || inputBuffer[i] == 254){
							i++;
							i++;
						}
					}
					else {
						printf("%c", inputBuffer[i]);
					}
				}
				// fflush(stdout);
				// fprintf(stderr, "%s\n", "Read the whole input!");
				fprintf(stderr, "Received %d bytes\n", (int)nread);
				outputBuffer[outputIndex] = '\0';
				for(int i = 0; outputBuffer[i]; i++) {
					printf("%d\n", (int)outputBuffer[i]);
				}
				if(outputIndex > 1)
				{
					ssize_t nsend = send(sockfd, outputBuffer, outputIndex, 0);
					if(nsend < 0) {
						fprintf(stderr, "%s\n", "Negotiation not done.");
					}
				}
			}
			fprintf(stderr, "%s\n", "Sent successfully");
		}
		else if(FD_ISSET(0, &readfds)) 
		{
			// printf("%s\n", );
			outputIndex = 0;
			fprintf(stderr, "%s\n", "Waiting for input: ");
			// fgets(readInput, DATASIZE - 10, 0);
			scanf ("%[^\n]%*c", readInput);
			for(int i = 0; readInput[i]; i++)
			{
				outputBuffer[outputIndex++] = readInput[i];
			}
	 		outputBuffer[outputIndex++] = '\r';
	 		outputBuffer[outputIndex++] = '\n';
	 		ssize_t nsend;
	 		nsend = send(sockfd, outputBuffer, outputIndex, 0);
	 		if(nsend < 0)
	 		{
	 			fprintf(stderr, "%s\n", "The data couldn't be send!");
	 		}
 		}
 		// FD_CLR(0, &readfds);
 		// FD_CLR(sockfd, &readfds);
 		fprintf(stderr, "Kuch toh hoja\n");
	}
	return 0;
}