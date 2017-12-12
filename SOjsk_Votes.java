import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import java.io.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class SOjsk_Votes {

	public static void main(String[] args) throws Exception {
		//声明Connection对象
        Connection con;
        //驱动程序名
        String driver = "com.mysql.jdbc.Driver";
        //URL指向要访问的数据库名mydata
        String url = "jdbc:mysql://192.168.3.123:3306/stack_overflow_2017_0831";
        //MySQL配置时的用户名
        String user = "SOjsk";
        //MySQL配置时的密码
        String password = "568321";
        //遍历查询结果集
        try {
            //加载驱动程序
            Class.forName(driver);
            //1.getConnection()方法，连接MySQL数据库！！
            con = DriverManager.getConnection(url,user,password);
            if(!con.isClosed())
                System.out.println("Succeeded connecting to the Database!");

            // 1.实例化SAXParserFactory对象
            SAXParserFactory factory = SAXParserFactory.newInstance();
            // 2.创建解析器
            SAXParser parser = factory.newSAXParser();
            // 3.获取需要解析的文档，生成解析器,最后解析文档
            File f = new File("/home/jsk/Stack Overflow Data/Votes.xml");
            SaxHandler dh = new SaxHandler();
            dh.initalMysql(con);
        
            parser.parse(f, dh);
        
            con.close();
        } catch(ClassNotFoundException e) {   
            //数据库驱动类异常处理
            System.out.println("Sorry,can`t find the Driver!");   
            e.printStackTrace();   
            } catch(SQLException e) {
            //数据库连接失败异常处理
            e.printStackTrace();  
            }catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
	}

}
