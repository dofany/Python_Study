BEGIN TRANSACTION;
CREATE TABLE phonebook(name varchar(10), phoneNum text);
INSERT INTO "phonebook" VALUES('tom','010-111-1111');
INSERT INTO "phonebook" VALUES('Johnson','010-222-2222');
INSERT INTO "phonebook" VALUES('jane','010-333-3333');
INSERT INTO "phonebook" VALUES('jerry','010-444-4444');
INSERT INTO "phonebook" VALUES('marry','010-555-5555');
COMMIT;
