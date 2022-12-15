import pymysql

conn = pymysql.connect(host="localhost", user="root", password="jiwi1234", db="candidseed", charset="utf8")
curs = conn.cursor()

# USERINFO 테이블 생성
print("[DB] 'userinfo' 테이블을 생성중입니다...")
sql = """CREATE TABLE `userinfo` (
	`USERID` INT(11) NOT NULL AUTO_INCREMENT,
	`email` TINYTEXT NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`password` TINYTEXT NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`nickname` TINYTEXT NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`userrank` BIT(1) NULL DEFAULT NULL,
	`createtime` DATETIME NULL DEFAULT NULL,
	PRIMARY KEY (`USERID`) USING BTREE
)
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;"""
curs.execute(sql)
print("[DB] 'userinfo' 생성완료!")

# wikitext 테이블 생성
print("[DB] 'wikitext' 테이블을 생성중입니다...")
sql = """CREATE TABLE `wikitext` (
	`TEXTID` INT(11) NOT NULL AUTO_INCREMENT,
	`text` MEDIUMTEXT NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`title` TINYTEXT NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`editnumber` SMALLINT(6) NOT NULL DEFAULT '1',
	`createtime` DATETIME NULL DEFAULT NULL,
	`count` MEDIUMINT(9) NULL DEFAULT NULL,
	PRIMARY KEY (`TEXTID`) USING BTREE
)
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;"""
curs.execute(sql)
print("[DB] 'wikitext' 생성완료!")

# recentchange 테이블 생성
print("[DB] 'recentchange' 테이블을 생성중입니다...")
sql = """CREATE TABLE `recentchange` (
	`ID` SMALLINT(6) NOT NULL AUTO_INCREMENT,
	`Title` INT(11) NULL DEFAULT NULL,
	`rnumber` INT(11) NULL DEFAULT NULL,
	`changer` VARCHAR(30) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`changetime` DATETIME NULL DEFAULT NULL,
	`count` MEDIUMINT(9) NULL DEFAULT NULL,
	PRIMARY KEY (`ID`) USING BTREE
)
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;"""
curs.execute(sql)
print("[DB] 'recentchange' 생성완료!")
conn.close()