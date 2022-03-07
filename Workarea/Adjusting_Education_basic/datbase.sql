DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS class;
DROP TABLE IF EXISTS itemBank;
DROP TABLE IF EXISTS itemBankRealWorld;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  fname TEXT NOT NULL,
  lname TEXT NOT NULL,
  mname TEXT,
  teacher BOOL NOT NULL,
  class_id TEXT UNIQUE NOT NULL
);

CREATE TABLE class (
  class_id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  teacher TEXT UNIQUE NOT NULL
);

CREATE TABLE itemBank (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id TEXT UNIQUE NOT NULL,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  feedback_wrong TEXT NOT NULL,
  feedback_right TEXT NOT NULL,
  real_world_id INTEGER NOT NULL
);

CREATE TABLE itemBankRealWorld (
  real_world_id INTEGER PRIMARY KEY AUTOINCREMENT,
  question TEXT UNIQUE NOT NULL
);