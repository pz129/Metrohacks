package project;

import org.jtwig.parser.*;
import static spark.Spark.before;

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
		Spark.port(1234);
		Spark.staticFileLocation("..");
		createRoutes();
	}
	protected void createRoutes() {
		Spark.get("/", new HomeController(this));
		Spark.get("/about-us", new AboutUsController());
		Spark.get("/dataset", new DataSetController());
		Spark.post("/",new HomeController(this));
		downloadGet("adsf.txt");
	}
	protected void downloadGet(String filename) {
		Spark.get("/download/"+filename, new DownloadController(filename));
	}
}
