--- Setup SQL for Hussar Solaris League

--- All Inner Sphere Chassis

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS chassis;

CREATE TABLE chassis (
        id INTEGER NOT NULL,
        name VARCHAR(64),
        weight INTEGER,
        class VARCHAR(7),
        trial_available BOOLEAN,
        PRIMARY KEY (id),
        UNIQUE (name),
        CHECK (class IN ('Light', 'Medium', 'Heavy', 'Assault')),
        CHECK (trial_available IN (0, 1))
);
INSERT INTO "chassis" VALUES(1,'Locust',20,'Light',0);
INSERT INTO "chassis" VALUES(2,'Commando',25,'Light',0);
INSERT INTO "chassis" VALUES(3,'Spider',30,'Light',1);
INSERT INTO "chassis" VALUES(4,'Urbanmech',30,'Light',0);
INSERT INTO "chassis" VALUES(5,'Jenner',35,'Light',0);
INSERT INTO "chassis" VALUES(6,'Raven',35,'Light',0);
INSERT INTO "chassis" VALUES(7,'Firestarter',35,'Light',0);
INSERT INTO "chassis" VALUES(8,'Panther',35,'Light',1);
INSERT INTO "chassis" VALUES(9,'Wolfhound',35,'Light',0);
INSERT INTO "chassis" VALUES(10,'Cicada',40,'Medium',0);
INSERT INTO "chassis" VALUES(11,'Blackjack',45,'Medium',0);
INSERT INTO "chassis" VALUES(12,'Vindicator',45,'Medium',0);
INSERT INTO "chassis" VALUES(13,'Phoenix Hawk',45,'Medium',0);
INSERT INTO "chassis" VALUES(14,'Centurion',50,'Medium',0);
INSERT INTO "chassis" VALUES(15,'Hunchback',50,'Medium',0);
INSERT INTO "chassis" VALUES(16,'Enforcer',50,'Medium',0);
INSERT INTO "chassis" VALUES(17,'Trebuchet',50,'Medium',0);
INSERT INTO "chassis" VALUES(18,'Crab',50,'Medium',1);
INSERT INTO "chassis" VALUES(19,'Kintaro',55,'Medium',0);
INSERT INTO "chassis" VALUES(20,'Shadowhawk',55,'Medium',0);
INSERT INTO "chassis" VALUES(21,'Griffin',55,'Medium',1);
INSERT INTO "chassis" VALUES(22,'Wolverine',55,'Medium',0);
INSERT INTO "chassis" VALUES(23,'Bushwacker',55,'Medium',0);
INSERT INTO "chassis" VALUES(24,'Dragon',60,'Heavy',1);
INSERT INTO "chassis" VALUES(25,'Quickdraw',60,'Heavy',0);
INSERT INTO "chassis" VALUES(26,'Rifleman',60,'Heavy',0);
INSERT INTO "chassis" VALUES(27,'Catapult',65,'Heavy',0);
INSERT INTO "chassis" VALUES(28,'Jagermech',65,'Heavy',0);
INSERT INTO "chassis" VALUES(29,'Thunderbolt',65,'Heavy',0);
INSERT INTO "chassis" VALUES(30,'Cataphract',70,'Heavy',0);
INSERT INTO "chassis" VALUES(31,'Grasshopper',70,'Heavy',1);
INSERT INTO "chassis" VALUES(32,'Warhammer',70,'Heavy',0);
INSERT INTO "chassis" VALUES(33,'Archer',70,'Heavy',0);
INSERT INTO "chassis" VALUES(34,'Orion',75,'Heavy',0);
INSERT INTO "chassis" VALUES(35,'Black Knight',75,'Heavy',0);
INSERT INTO "chassis" VALUES(36,'Marauder',75,'Heavy',0);
INSERT INTO "chassis" VALUES(37,'Awesome',80,'Assault',0);
INSERT INTO "chassis" VALUES(38,'Victor',80,'Assault',0);
INSERT INTO "chassis" VALUES(39,'Zeus',80,'Assault',1);
INSERT INTO "chassis" VALUES(40,'Battlemaster',85,'Assault',0);
INSERT INTO "chassis" VALUES(41,'Stalker',85,'Assault',1);
INSERT INTO "chassis" VALUES(42,'Highlander',90,'Assault',0);
INSERT INTO "chassis" VALUES(43,'Mauler',90,'Assault',0);
INSERT INTO "chassis" VALUES(44,'Cyclops',90,'Assault',0);
INSERT INTO "chassis" VALUES(45,'Banshee',95,'Assault',0);
INSERT INTO "chassis" VALUES(46,'Atlas',100,'Assault',0);
INSERT INTO "chassis" VALUES(47,'King Crab',100,'Assault',0);

-- Settings

DROP TABLE IF EXISTS settings;

CREATE TABLE settings (
        name VARCHAR(64) NOT NULL,
        value VARCHAR(64),
        PRIMARY KEY (name)
);

INSERT INTO "settings" VALUES('maintenance','0');

COMMIT;