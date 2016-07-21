CREATE TABLE user (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(25) NOT NULL,
  email varchar(50) DEFAULT NULL,
  password varchar(32) NOT NULL,
  role varchar(25) NOT NULL,
  cname varchar(25) DEFAULT NULL,
  url varchar(50) DEFAULT NULL,
  token varchar(32) DEFAULT NULL,
  extra varchar(500) DEFAULT NULL,
  PRIMARY KEY (id,username));


CREATE TABLE vm_assets (
  id int(11) NOT NULL AUTO_INCREMENT,
  ip_addr varchar(25) NOT NULL,
  app_name varchar(25) DEFAULT NULL,
  hostname varchar(25) DEFAULT NULL,
  vc_name varchar(25) DEFAULT NULL,
  cpu varchar(25) DEFAULT NULL,
  memory varchar(25) DEFAULT NULL,
  disk varchar(25) DEFAULT NULL,
  os varchar(25) DEFAULT NULL,
  status varchar(25) DEFAULT NULL,
  office_name varchar(25) DEFAULT NULL,
  office_contact varchar(25) DEFAULT NULL,
  office_phone varchar(25) DEFAULT NULL,
  object_contact varchar(25) DEFAULT NULL,
  object_phone varchar(25) DEFAULT NULL,
  create_date varchar(25) DEFAULT NULL,
  end_date varchar(25) DEFAULT NULL,
  notes varchar(25) DEFAULT NULL,
  PRIMARY KEY (id,ip_addr));