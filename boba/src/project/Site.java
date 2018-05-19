package project;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.websocket.server.WebSocketHandler;
import org.eclipse.jetty.websocket.servlet.WebSocketServletFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import spark.Spark;
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
		makeWebSocket();
		Spark.get("/", new HomeController(this));
		Spark.get("/about-us", new AboutUsController());
		Spark.get("/dataset", new DataSetController());
		Spark.post("/",new HomeController(this));
		downloadGet("adsf.txt");
	}
	protected void makeWebSocket() {
		Server server = new Server(8080);
        WebSocketHandler wsHandler = new WebSocketHandler() {
            @Override
            public void configure(WebSocketServletFactory factory) {
                factory.register(AudioStream.class);
            }
        };
        server.setHandler(wsHandler);
        try {
			server.start();
			server.join();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	protected void downloadGet(String filename) {
		Spark.get("/download/"+filename, new DownloadController(filename));
	}
}
