import java.io.*;
import java.net.*;

class Packet implements Serializable
{
	private int MSG_TYPE;
	private int seqNum;
	private boolean is_corrupt;
	private boolean is_lost;

	public Packet(int msg_type, int sno)
	{
		this.MSG_TYPE = msg_type;
		this.seqNum = sno;
		this.is_lost = false;
		this.is_corrupt = false;
	}

	public int getType()
	{
		return this.MSG_TYPE;
	}

	public int getSequenceNo()
	{
		return this.seqNum;
	}


	public static byte[] getBytes(Packet p) throws IOException
	{
		ByteArrayOutputStream b = new ByteArrayOutputStream();
		ObjectOutputStream o = new ObjectOutputStream(b);
		o.writeObject(p);
		return b.toByteArray();
	}

	public static Object getObject(byte[] bArr) throws IOException, ClassNotFoundException
	{
		ByteArrayInputStream b = new ByteArrayInputStream(bArr);
		ObjectInputStream i = new ObjectInputStream(b);
		return (Packet)i.readObject();
	}

	public void setCorrupt()
	{
		this.is_corrupt = true;
	}

	public void setLost()
	{
		this.is_lost = true;
	}

	public void setCorrect()
	{
		this.is_lost = false;
		this.is_corrupt = false;
	}

	public Boolean checkCorrupt()
	{
		return this.is_corrupt;
	}

	public Boolean checkLost()
	{
		return this.is_lost;
	}
}