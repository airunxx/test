import os
import smtplib
 
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
from_addr = formataddr(('Google Dochi', 'dbf5032mb@google.com')) #보내는사람
to_addr = formataddr(('Naver Dochi', 'dbf5032mb@naver.com')) #받는사람
 
session = None
try:
    # SMTP 세션 생성
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.set_debuglevel(True)
    
    # SMTP 계정 인증 설정
    session.ehlo()
    session.starttls()
    session.login('dbf5032mb@gmail.com', 'zlpgerdhyadypxxz')
 
    # 메일 콘텐츠 설정
    message = MIMEMultipart("alternative")
    
    # 메일 송/수신 옵션 설정
    message.set_charset('utf-8')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = '안녕하세요'
 
    # 메일 콘텐츠 - 내용
    body = '''
    <p><span style="font-size:14px;margin-left:0.8ex;font-family:arial,'Apple SD Gothic Neo','Malgun Gothic','맑은 고딕',sans-serif"><br></span></p><blockquote style="font-size:14px;border-left-style:solid;border-left-width:2px;margin-bottom:0pt;margin-left:0.8ex;margin-right:0pt;margin-top:0pt;padding-left:1ex;"><div style="font-family:arial,'Apple SD Gothic Neo','Malgun Gothic','맑은 고딕',sans-serif;"><div style="color:#111;font-family:Apple SD Gothic Neo,Malgun Gothic,'맑은 고딕',sans-serif;font-size:10pt;line-height:1.5;"><div><div><div bgcolor="#f6f6f6" style="background:#f6f6f6;margin:0;padding:0"><p></p><table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" style="background:#f6f6f6">
    <tbody>
    <tr>
    <td>
    
    <table role="presentation" width="650" border="0" cellspacing="0" cellpadding="0" align="center" style="margin-left:auto;margin-right:auto">
    
    <tbody>
    
    <tr>
    <td>
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse">
    <tbody><tr>
    <td>
    
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap;background-color:#ffffff">
    <td style="border-top:10px solid #f5821f;white-space:normal;padding-top:25px;padding-left:40px;padding-bottom:25px;padding-right:40px;background-color:#ffffff">
    
    <table role="presentation" width="48%" border="0" cellpadding="0" cellspacing="0" align="left">
    <tbody>
    <tr>
    <td>
    <div>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tbody>
    <tr>
    <td><a href="https://jichanwiki.site" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.cloudflare.com/&amp;source=gmail&amp;ust=1623662822386000&amp;usg=AFQjCNEknxfP15v0CBMDeOYdjVOcslsiAg" rel="noopener noreferrer"><img src="https://jichanwiki.site//image/5d6ae5a75dd24682f117f7d09c632c9c41c431dba8b35a8db72b1f56.svg" alt="" height="" width="260" style="border-style:none"></a></td>
    </tr>
    </tbody>
    </table>
    </div> </td>
    </tr>
    </tbody>
    </table>
    
    
    <table role="presentation" width="48%" border="0" cellpadding="0" cellspacing="0" align="right">
    <tbody>
    <tr>
    <td style="text-align:right;color:#333333;font-family:Open Sans,Helvetica,Arial,sans-serif;font-size:14px;line-height:20px">
    <div></div> </td>
    </tr>
    </tbody>
    </table>
     </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    <tr>
    <td>
    
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap;background-color:#ffffff">
    <td style="color:#333333;text-align:left;white-space:normal;font-family:Open Sans,Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;padding-left:40px;padding-right:40px;background-color:#ffffff;font-weight:lighter">
    <div>
    
      <p style="text-align: right;">회원가입 인증관련 이메일</p>
    <p>
    </p><hr><br><p></p>
    <p>안녕하세요. 귀하의 이메일계정으로 지찬위키 회원가입이 요청되어 인증 이메일을 발송합니다</p>
    <p><br></p>
    <p>만약 본인이 아니라면 이 메일을 무시해주세요.</p>
    <p><br></p>
    <p><br></p>
    <p>인증 코드 및 주소는 다음과 같습니다</p>
    <p><br><br></p>
    <p>{{}}</p></div> </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    
    
    
    
    <tr>
    <td>
    
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap;background-color:#ffffff">
    <td height="25" style="background-color:#ffffff;line-height:25px;font-size:25px"> &nbsp; <br><br></td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    <tr>
    <td>
    
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap;background-color:#ffffff">
    <td height="25" style="white-space:normal;background-color:#ffffff;line-height:25px;font-size:25px"> &nbsp; </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    <tr>
    <td>
    
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap;background-color:#f6f6f6">
    <td height="25" style="white-space:normal;background-color:#f6f6f6;line-height:25px;font-size:25px"> &nbsp; </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    <tr>
    <td>
    
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap">
    <td style="white-space:normal;padding-left:40px;padding-right:40px">
    <div>
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0">
    <tbody>
    <tr>
    <td style="font-family:Arial,Helvetica,sans-serif;color:#8f8f8f;font-size:13px;text-align:center"><p>Copyright © 2020 ~ Jichanwiki.<br>Distribute&nbsp;in Tokyo, Japen | Operated by Team Lwnlcks<br><br>jichanwiki.site</p></td>
    </tr>
    <tr>
    <td style="padding-top:30px" align="center"><p>
     </p></td>
    </tr>
    </tbody>
    </table>
    </div> </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    <tr>
    <td>
    
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    
    <tbody>
    <tr style="white-space:nowrap;background-color:#f6f6f6">
    <td height="25" style="white-space:normal;background-color:#f6f6f6;line-height:25px;font-size:25px"> &nbsp; </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    </tbody></table> </td>
    </tr>
    
    
    <tr>
    <td>
    <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="min-width:100%">
    <tbody>
    <tr style="white-space:nowrap;background-color:#ffffff">
    <td height="1" style="min-width:650px;opacity:0;font-size:0px;line-height:0px"> <img height="1" src="#m_-6285867222191677894_" style="min-width:650px;max-height:0px;text-decoration:none;border:none"> </td>
    </tr>
    </tbody>
    </table> </td>
    </tr>
    
    </tbody>
    </table>
     </td>
    </tr>
    </tbody>
    </table></div></div></div></div></div></blockquote><p><br></p>
    '''
    bodyPart = MIMEText(body, 'html', 'utf-8')
    message.attach( bodyPart )
 
    # 메일 발송
    session.sendmail(from_addr, to_addr, message.as_string())            
 
    print( 'Successfully sent the mail!!!' )
except Exception as e:
    print( e )
finally:
    if session is not None:
        session.quit()
