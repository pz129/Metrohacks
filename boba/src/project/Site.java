package project;

import static spark.Spark.*;

import spark.Route;
import spark.Spark;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
public class Site {
	public static final transient Logger log=LoggerFactory.getLogger(Site.class);
	public static void main(String[] args) {
		Site site=new Site();
		site.initWebsite();
		log.info("setup complete");
	}
	protected void initWebsite() {
		port(1234);
		staticFileLocation("..");
		createRoutes();
	}
	protected void createRoutes() {
		get("/", new HomeController());
		post("/",new HomeController());
	}
}
