package project;
import static spark.Spark.before;

import spark.Request;
import spark.Response;
import spark.Route;
import spark.Spark;
public class HomeController implements Route{

	public Object handle(Request request, Response response) throws Exception {
		System.out.println("go");
		return "Hello";
	}

}
