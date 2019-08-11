import package;
import fogtorch.infrastructure.Infrastructure;
import fogtorch.utils.Hardware;
import static java.util.Arrays.asList;
 public class  LTinfrastructure{ 
	 public static Infrastructure createInfrastructure() { 
 	 	 Infrastructure I = new Infrastructure();
			 I.addCloudDatacentre("Cloud_1",asList("mySQL",".NET","C++" ),12.12,11.23);
			 I.addCloudDatacentre("Cloud_2",asList("spark","linux","ruby" ),44.123896,-122.781555);
			 I.addFogNode("fog_3",asList("python","C++" ),new Hardware(0,2,0),12333.12,1231.122);
			 I.addFogNode("fog_1",asList("python","C++" ),new Hardware(0,4,0),23312.22,1333.21);
			 I.addLink("fog_1","fog_2",1,100);
			 I.addLink("fog_1","fog_3",5,20);
			 I.addThing("videocamera0","videocamera",43.78882,10.12333);



		return I;
 		} 
 	 }