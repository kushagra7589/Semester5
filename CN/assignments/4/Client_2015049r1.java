import java.net.*;
import java.io.*;

class ServerResponse extends Thread {
	private Socket cs;
	private DataInputStream serverRead;
	private int shouldIStop;

	public ServerResponse(Socket cs, DataInputStream sr, int stop)
	{
		this.cs = cs;
		this.serverRead = sr;
		this.shouldIStop = stop;

	}

	public void run()
	{
		String line;
		try
		{
			while((line = this.serverRead.readLine()) != null)
			{
				System.out.println(line);
				if(this.shouldIStop == 1)
				{
					break;
				}
			}
			this.cs.close();
		}
		catch (IOException e)
		{
			System.out.println("Connection closed by foreign host.");
		}
		catch (Exception e)
		{
			System.out.println("Client exited!");
		}
	}
}

class ChatClient {
	private Socket clientSocket;
	private BufferedReader userInput;
	private DataInputStream serverRead;
	private PrintStream serverWrite;
	private int shouldIStop;

	public ChatClient(int pno, String hn)
	{
		try
		{
			this.clientSocket = new Socket(hn, pno);
			this.userInput = new BufferedReader(new InputStreamReader(System.in));
			this.serverRead = new DataInputStream(this.clientSocket.getInputStream());
			this.serverWrite = new PrintStream(this.clientSocket.getOutputStream());	
			this.shouldIStop = 0;
		}
		catch (IOException e)
		{
			System.out.println(e);
		}
	}

	public static void main(String args[])
	{
		if(args.length < 2)
		{
			System.out.println("Usage: java ChatClient <hostname> <portno>");
			return;
		}
		int portno = Integer.parseInt(args[1]);
		String hostname = args[0];
		try
		{
			ChatClient cc = new ChatClient(portno, hostname);

			// to take input from the server
			ServerResponse readResonse = new ServerResponse(cc.clientSocket, cc.serverRead, cc.shouldIStop);
			readResonse.start();

			// to send request to the server -> take user input and send it to server
			while(true)
			{
				String line = cc.userInput.readLine();
				cc.serverWrite.println(line);
				if(line.startsWith("exit"))
				{
					cc.shouldIStop = 1;
					break;
				}
			}

			// now closing all connections
			cc.userInput.close();
			cc.serverRead.close();
			cc.serverWrite.close();
			cc.clientSocket.close();
		}
		catch (IOException f)
		{
			System.out.println(f);			
		}
		
	}
}
