import java.sql.*;
import java.util.ArrayList;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class SaxHandler_QA extends DefaultHandler {
private Connection con;
private Statement stmt;
private ResultSet rs;
	
	public void initalMysql(Connection cc){
		this.con = cc;
		try {
			this.stmt = this.con.createStatement();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public void closeMysql() throws SQLException{
		this.con.close();
		this.stmt.close();
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
		try {
			PreparedStatement psql;
			PreparedStatement psql2; 
			//预处理添加数据，其中有两个参数--“？”
			if (arg3.getValue("PostTypeId").equals("1")) { //ques
				psql = con.prepareStatement("insert into questions (Id,CreationDate,AcceptedAnswerId,Score,ViewCount,TagId1,TagId2,TagId3,TagId4,TagId5,AnswerCount,CommentCount,FavoriteCount) "
						+ "values(?,?,?,?,?,?,?,?,?,?,?,?,?)");
				psql.setInt(1, Integer.parseInt(arg3.getValue("Id")));									//set from index 1
				psql.setString(2, arg3.getValue("CreationDate"));
				psql.setInt(3, Integer.parseInt(arg3.getValue("AcceptedAnswerId")==null?"-1":arg3.getValue("AcceptedAnswerId")));
				psql.setInt(4, Integer.parseInt(arg3.getValue("Score")));
				psql.setInt(5, Integer.parseInt(arg3.getValue("ViewCount")));

				psql.setInt(11, Integer.parseInt(arg3.getValue("AnswerCount")));
				psql.setInt(12, Integer.parseInt(arg3.getValue("CommentCount")));
				psql.setInt(13, Integer.parseInt(arg3.getValue("FavoriteCount")==null?"0":arg3.getValue("FavoriteCount")));
				
				ArrayList<String> tagNames = new ArrayList<String>();
				ArrayList<Integer> tagIds = new ArrayList<Integer>();
				char[] Tags = arg3.getValue("Tags").toCharArray(); // &lt;c#&gt;&lt;winforms&gt;&lt;type-conversion&gt;&lt;decimal&gt;&lt;opacity&gt;
				int i = 0;
				while (i < Tags.length){ // &lt;c#&gt;
					i += 1;
					String tagName = "";
					while (Tags[i] != '>'){ 
						tagName += Tags[i];
						i += 1;
					}
					tagNames.add(tagName);
					i += 1;
				}
				for (String tagName : tagNames){
					try{
						stmt = con.createStatement(); //创建Statement对象
			            String sql = "select Id from tags where TagName=\"" + tagName + "\"";    //检索tags表得到tag的Id
			            rs = stmt.executeQuery(sql);//创建数据对象	
			            rs.next();
			            tagIds.add(rs.getInt(1));
			            rs.close();
			        }catch(Exception e){
			            e.printStackTrace();
			        }
					
				}
				psql2 = con.prepareStatement("insert into post2Tag (PostId,TagId1,TagId2,TagId3,TagId4,TagId5) "
						+ "values(?,?,?,?,?,?)");
				psql2.setInt(1, Integer.parseInt(arg3.getValue("Id")));
				for (i = 0;i < Math.min(tagIds.size(),5);i++){
					psql.setInt(i+6, tagIds.get(i));
					psql2.setInt(i+2, tagIds.get(i));
				}
				for (;i<5;i++){
					psql.setInt(i+6, -1);
					psql2.setInt(i+2, -1);
				}
				System.out.println("ques\t"+arg3.getValue("Id") + "\t"+psql.executeUpdate());           //执行更新ques
				System.out.println("post2Tag\t"+arg3.getValue("Id") + "\t"+psql2.executeUpdate());           //执行更新post2Tag
			}
			else if (arg3.getValue("PostTypeId").equals("2")) { //ans
				psql = con.prepareStatement("insert into answers (Id,CreationDate,ParentId,Score,CommentCount) "
						+ "values(?,?,?,?,?)");
				psql.setInt(1, Integer.parseInt(arg3.getValue("Id")));									//set from index 1
				psql.setString(2, arg3.getValue("CreationDate"));
				psql.setInt(3, Integer.parseInt(arg3.getValue("ParentId")));
				psql.setInt(4, Integer.parseInt(arg3.getValue("Score")));
				psql.setInt(5, Integer.parseInt(arg3.getValue("CommentCount")));
				System.out.println("ans\t"+arg3.getValue("Id") + "\t"+psql.executeUpdate());           //执行更新		

				ArrayList<Integer> tagIds = new ArrayList<Integer>();
				try{
					stmt = con.createStatement(); //创建Statement对象
				    String sql = "select * from post2Tag where PostId=\"" + arg3.getValue("ParentId") + "\"";    //检索post2Tag表得到parent question
				    rs = stmt.executeQuery(sql);//创建数据对象
				    for (int i = 0;i < 5;i++){
				    	tagIds.add(rs.getInt(i+1));
				    }
			        rs.close();
				}catch(Exception e){
				    e.printStackTrace();
				}
					
				psql2 = con.prepareStatement("insert into post2Tag (PostId,TagId1,TagId2,TagId3,TagId4,TagId5) "
						+ "values(?,?,?,?,?,?)");
				psql2.setInt(1, Integer.parseInt(arg3.getValue("Id")));
				for (int i = 0;i < 5;i++){
					psql2.setInt(i+2, tagIds.get(i));
				}
				System.out.println("post2Tag\t"+arg3.getValue("Id") + "\t"+psql2.executeUpdate());           //执行更新post2Tag
			}else{ // PostTypeId = 4 taginfomation
				System.out.println(arg3.getValue("Id")+" : "+"Orther PostTypeId:"+arg3.getValue("PostTypeId"));
			}
		} catch(SQLException e) {
			//数据库异常处理
			e.printStackTrace(); 
	    } catch(Exception e){
	        e.printStackTrace();
	    }

		/*
		System.out.println("开始解析元素 " + arg2);
		if (arg3 != null) {
			for (int i = 0; i < arg3.getLength(); i++) {
				// getQName()是获取属性名称，
				System.out.println(arg3.getQName(i) + "=\"" + arg3.getValue(i) + "\"");
			}
		}
		System.out.print(arg2 + ":");
		*/
		
		super.startElement(arg0, arg1, arg2, arg3);
	}
}
