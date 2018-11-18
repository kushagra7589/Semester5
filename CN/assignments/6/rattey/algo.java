import java.util.*;

class Pair
{
	public int first;
	public int second;

	public Pair()
	{
		this.first = 0;
		this.second = 0;
	}

	public Pair(int x, int y)
	{
		this.first = x;
		this.second = y;
	}

	public String toString()
	{
		return "(" + this.first + " -> " + this.second + ")";
	}
}

class Parser
{
	private String input;
	private HashMap<String, Integer> index;
	private HashMap<Integer, String> rev;
	private HashMap<Integer, ArrayList<Pair> > graph;
	
	public Parser(String inp)
	{
		this.input = inp;
		graph = new HashMap<Integer, ArrayList<Pair> >();
		this.index = new HashMap<String, Integer>();
		String[] splitted = inp.split(" ");
		int n = 0;
		while(!(splitted[n].equals("#")))
		{
			n += 1;
		}
		n -= 1;
		int ind = 0;
		for(int i = 0; i < n; i += 3)
		{
			String x = splitted[i];
			String y = splitted[i + 1];
			if(!index.containsKey(x))
			{
				index.put(x, ind);
				rev.put(ind, x);
				ind += 1;
			}
			if(!index.containsKey(y))
			{
				index.put(y, ind);
				rev.put(ind, y);
				ind += 1;
			}
			Integer w = Integer.parseInt(splitted[i + 2]);
			Integer X = index.get(x);
			Integer Y = index.get(y);
			if(!graph.containsKey(X))
			{
				graph.put(X, new ArrayList<Pair>());
			}
			if(!graph.containsKey(Y))
			{
				graph.put(Y, new ArrayList<Pair>());
			}
			ArrayList<Pair> adjX = this.graph.get(X);
			ArrayList<Pair> adjY = this.graph.get(Y);
			adjX.add(new Pair(Y, w));
			adjY.add(new Pair(X, w));
			graph.put(X, adjX);
			graph.put(Y, adjY);
		}
		System.out.println(Arrays.asList(index));
	}

	public HashMap<Integer, ArrayList<Pair> > returnGraph() { return this.graph; }

	public void updateGraph(String inp)
	{
		String[] splitted = inp.split(" ");
		String x = splitted[0];
		Integer X = this.index.get(x);
		String y = splitted[1];
		Integer Y = this.index.get(y);
		Integer w = Integer.parseInt(splitted[2]);
		
		if(!graph.containsKey(X))
		{
			this.graph.put(X, new ArrayList<Pair>());
		}
		if(!graph.containsKey(Y))
		{
			this.graph.put(Y, new ArrayList<Pair>());
		}

		ArrayList<Pair> adjX = this.graph.get(X);
		ArrayList<Pair> adjY = this.graph.get(Y);

		adjX.add(new Pair(Y, w));
		adjY.add(new Pair(X, w));
		
		this.graph.put(X, adjX);
		this.graph.put(Y, adjY);
	}

	public static void main(String args[])
	{
		Scanner reader = new Scanner(System.in);

		Parser prsr = new Parser("A B 1 B C 12 A C 10 D C 9 #");
		HashMap<Integer, ArrayList<Pair> > gr = prsr.returnGraph();
		System.out.println(Arrays.asList(gr));

		Dijkstra sd = new Dijkstra(gr);

		for(Integer k : gr.keySet())
		{
			sd.shortestDistance(k);
		}
	}
}

class Dijkstra
{
	private HashMap<Integer, ArrayList<Pair> > graph;
	private HashMap<Integer, HashMap<Integer, Integer> > dist;
	private HashMap<Integer, String> node;
	private HashMap<Integer, Integer> routing_table;
	private final int N = 100000000; 
	public Dijkstra(HashMap<Integer, ArrayList<Pair> > g, HashMap<Integer, String> rev)
	{
		this.graph = g;
		this.node = rev;
		this.routing_table = new HashMap<Integer, Integer>();
		this.dist = new HashMap<Integer, HashMap<Integer, Integer> >();
		for(Integer i : this.graph.keySet())
		{
			HashMap<Integer, Integer> temp = new HashMap<Integer, Integer>();
			for(Integer j : this.graph.keySet())
			{
				temp.put(j, N);
			}
			this.dist.put(i, temp);
		}
	}

	public void shortestDistance(Integer source)
	{
		System.out.println("------------------------------------------------------------------------------------------------");
		System.out.println("------------------------------------------------------------------------------------------------");
		System.out.println("\t\tSOURCE : " + source);
		HashMap<Integer, Integer> temp = new HashMap<Integer, Integer>();
		temp.put(source, 0);
		HashMap<Integer, Integer> curr_dist = this.dist.get(source);
		curr_dist.put(source, 0);
		ArrayList<Pair> adjS = this.graph.get(source);
		for(Pair p : adjS)
		{
			curr_dist.put(p.first, p.second);
			routing_table.put(p.first, source);
		}
		while(temp.size() < this.graph.keySet().size())
		{
			int m = this.N;
			int v = 0;
			for(Integer j : this.graph.keySet())
			{
				if(!temp.containsKey(j) && curr_dist.get(j) < m)
				{
					m = curr_dist.get(j);
					v = j;
				}
			}
			System.out.println("Min distance node = " + node.get(v) + " with distance " + m);
			ArrayList<Pair> adj = this.graph.get(v);
			for(Pair p : adj)
			{
				if(!temp.containsKey(p.first))
				{
					if(curr_dist.get(p.first) > p.second + curr_dist.get(v))
					{
						routing_table.put(p.first, v);
						int updated = p.second + curr_dist.get(v);
						System.out.println("The distance of " + this.node.get(p.first) + " has been updated from " + curr_dist.get(p.first) + " to " + updated);
						curr_dist.put(p.first, p.second + curr_dist.get(v));
					}
				}
			}
			temp.put(v, 0);
		}

		System.out.println("\tROUTING TABLE");
		Iterator<Integer> it = graph.keySet().iterator();
		while(it.hasNext())
		{
			Integer destination = it.next();
			System.out.print(this.node.get(destination));
			Integer parent = destination;
			while(parent != source)
			{
				parent = routing_table.get(parent);
				System.out.print(" ---> " + this.node.get(parent));
			}
			System.out.println("");
		}
		this.dist.put(source, curr_dist);
	}
}