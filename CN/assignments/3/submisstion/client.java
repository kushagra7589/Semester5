import java.net.*;
import java.io.*;

class ServerResponse extends Thread {
	private Socket cs;
	private DataInputStream serverRead;

	public ServerResponse(Socket cs, DataInputStream sr)
	{
		this.cs = cs;
		this.serverRead = sr;
	}

	public void run()
	{
		String line;
		try
		{
			while((line = this.serverRead.readLine()) != null)
			{
				System.out.println(line);
				if(line.indexOf("leaving!") != -1)
				{
					break;
				}
			}
			this.cs.close();
		}
		catch (IOException e)
		{
			System.out.println(e);
		}
	}
}

class ChatClient {
	private Socket clientSocket;
	private BufferedReader userInput;
	private DataInputStream serverRead;
	private PrintStream serverWrite;

	public ChatClient(int pno, String hn)
	{
		try
		{
			this.clientSocket = new Socket(hn, pno);
			this.userInput = new BufferedReader(new InputStreamReader(System.in));
			this.serverRead = new DataInputStream(this.clientSocket.getInputStream());
			this.serverWrite = new PrintStream(this.clientSocket.getOutputStream());	
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
			ServerResponse readResonse = new ServerResponse(cc.clientSocket, cc.serverRead);
			readResonse.start();

			// to send request to the server -> take user input and send it to server
			while(true)
			{
				String line = cc.userInput.readLine();
				cc.serverWrite.println(line);
				if(line.startsWith("exit"))
				{
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