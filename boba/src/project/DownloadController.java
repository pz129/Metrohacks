package project;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.servlet.http.HttpServletResponse;

import spark.Request;
import spark.Response;
import spark.Route;

public class DownloadController implements Route {
	String filename;
	DownloadController(String filename){
		this.filename=filename;
	}
	public Object handle(Request request, Response response) throws Exception {
		Path path= Paths.get("/src/sheets/"+filename);
		byte[] data=null;
		try {
			data=Files.readAllBytes(path);
		}catch(Exception e1) {
			e1.printStackTrace();
		}
		 HttpServletResponse raw = response.raw();
	        response.header("Content-Disposition", "attachment; filename="+filename);
	        response.type("application/force-download");
	        try {
	            raw.getOutputStream().write(data);
	            raw.getOutputStream().flush();
	            raw.getOutputStream().close();
	        } catch (Exception e) {

	            e.printStackTrace();
	        }
	        return raw;
	}

}
