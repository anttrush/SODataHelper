import org.xml.sax.helpers.DefaultHandler;
import org.xml.sax.*;
import java.sql.*;

public class SaxHandler extends DefaultHandler {
private Connection con;
private PreparedStatement psql;
	
	public void initalMysql(Connection cc){
		this.con = cc;
	}
	
	public void closeMysql() throws SQLException{
		this.con.close();
	}
	
	
	/* 此方法有三个参数
    arg0是传回来的字符数组，其包含元素内容
    arg1和arg2分别是数组的开始位置和结束位置 */
	@Override
	public void characters(char[] arg0, int arg1, int arg2) throws SAXException {
		//String content = new String(arg0, arg1, arg2);
		//System.out.println(content);
		super.characters(arg0, arg1, arg2);
	}

	@Override
	public void endDocument() throws SAXException {
		System.out.println("\n…………结束解析文档…………");
		super.endDocument();
	}

	/* arg0是名称空间
    arg1是包含名称空间的标签，如果没有名称空间，则为空
    arg2是不包含名称空间的标签 */
	@Override
	public void endElement(String arg0, String arg1, String arg2)
			throws SAXException {
		//System.out.println("结束解析元素  " + arg2);
		super.endElement(arg0, arg1, arg2);
	}

	@Override
	public void startDocument() throws SAXException {
		System.out.println("…………开始解析文档…………\n");
		super.startDocument();
	}

	/*arg0是名称空间
   	arg1是包含名称空间的标签，如果没有名称空间，则为空
   	arg2是不包含名称空间的标签
   	arg3很明显是属性的集合 */
	@Override
	public void startElement(String arg0, String arg1, String arg2,
			Attributes arg3) throws SAXException {
		// TODO Auto-generated method stub
		        //遍历查询结果集
		if (arg2 == "row" && Integer.parseInt(arg3.getValue("Id")) > 248793){
			try {
				//预处理添加数据，其中有两个参数--“？”
				psql = con.prepareStatement("insert into votes (Id,PostId,VoteTypeId,CreationDate) "
						+ "values(?,?,?,?)");
				for (int i = 0;i < 3;i++){
					psql.setInt(i+1, Integer.parseInt(arg3.getValue(i)));              //设置参数i(从1开始)
				}
				psql.setString(4, arg3.getValue(3));
				System.out.println("votes\t"+arg3.getValue("Id") + "\t"+psql.executeUpdate());           //执行更新
			} catch(SQLException e) {
				//数据库异常处理
				e.printStackTrace();  
            }
		}

		/*
		System.out.println("开始解析元素 " + arg2);
		if (arg3 != null) {
			for (int i = 0; i < arg3.getLength(); i++) {
				// getQName()是获取属性名称，
				System.out.print(arg3.getQName(i) + "=\"" + arg3.getValue(i) + "\"");
			}
		}
		System.out.print(arg2 + ":");
		*/
		super.startElement(arg0, arg1, arg2, arg3);
	}
}
