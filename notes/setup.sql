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

-- Variants

DROP TABLE IF EXISTS variant;

CREATE TABLE variant (
	id INTEGER NOT NULL, 
	name VARCHAR(64), 
	chassis_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(chassis_id) REFERENCES chassis (id)
);
INSERT INTO "variant" VALUES(1,'LCT-3V',1);
INSERT INTO "variant" VALUES(2,'PIRATES'' BANE',1);
INSERT INTO "variant" VALUES(3,'LCT-1E',1);
INSERT INTO "variant" VALUES(4,'LCT-1M',1);
INSERT INTO "variant" VALUES(5,'LCT-1V',1);
INSERT INTO "variant" VALUES(6,'LCT-3M',1);
INSERT INTO "variant" VALUES(7,'LCT-3S',1);
INSERT INTO "variant" VALUES(8,'COM-1B',2);
INSERT INTO "variant" VALUES(9,'COM-2D',2);
INSERT INTO "variant" VALUES(10,'COM-1D',2);
INSERT INTO "variant" VALUES(11,'COM-3A',2);
INSERT INTO "variant" VALUES(12,'DEATH''S KNELL',2);
INSERT INTO "variant" VALUES(13,'ANANSI',3);
INSERT INTO "variant" VALUES(14,'SDR-5K',3);
INSERT INTO "variant" VALUES(15,'SDR-5D',3);
INSERT INTO "variant" VALUES(16,'SDR-5V',3);
INSERT INTO "variant" VALUES(17,'UM-R60',4);
INSERT INTO "variant" VALUES(18,'UM-R60L',4);
INSERT INTO "variant" VALUES(19,'UM-R63',4);
INSERT INTO "variant" VALUES(20,'UM-K9',4);
INSERT INTO "variant" VALUES(21,'EMBER',7);
INSERT INTO "variant" VALUES(22,'FS9-A',7);
INSERT INTO "variant" VALUES(23,'FS9-H',7);
INSERT INTO "variant" VALUES(24,'FS9-K',7);
INSERT INTO "variant" VALUES(25,'FS9-S',7);
INSERT INTO "variant" VALUES(26,'JR7-D',5);
INSERT INTO "variant" VALUES(27,'JR7-F',5);
INSERT INTO "variant" VALUES(28,'JR7-K',5);
INSERT INTO "variant" VALUES(29,'OXIDE',5);
INSERT INTO "variant" VALUES(30,'PNT-10K',8);
INSERT INTO "variant" VALUES(31,'PNT-10P',8);
INSERT INTO "variant" VALUES(32,'PNT-8Z',8);
INSERT INTO "variant" VALUES(33,'PNT-9R',8);
INSERT INTO "variant" VALUES(34,'PNT-KK',8);
INSERT INTO "variant" VALUES(35,'HUGINN',6);
INSERT INTO "variant" VALUES(36,'RVN-2X',6);
INSERT INTO "variant" VALUES(37,'RVN-3L',6);
INSERT INTO "variant" VALUES(38,'RVN-4X',6);
INSERT INTO "variant" VALUES(39,'WLF-1',9);
INSERT INTO "variant" VALUES(40,'WLF-1A',9);
INSERT INTO "variant" VALUES(41,'WLF-1B',9);
INSERT INTO "variant" VALUES(42,'WLF-2',9);
INSERT INTO "variant" VALUES(43,'WLF-GR',9);
INSERT INTO "variant" VALUES(44,'CDA-2A',10);
INSERT INTO "variant" VALUES(45,'CDA-2B',10);
INSERT INTO "variant" VALUES(46,'CDA-3C',10);
INSERT INTO "variant" VALUES(47,'CDA-3F',10);
INSERT INTO "variant" VALUES(48,'CDA-3M',10);
INSERT INTO "variant" VALUES(49,'X-5',10);
INSERT INTO "variant" VALUES(50,'ARROW',11);
INSERT INTO "variant" VALUES(51,'BJ-1',11);
INSERT INTO "variant" VALUES(52,'BJ-1DC',11);
INSERT INTO "variant" VALUES(53,'BJ-1X',11);
INSERT INTO "variant" VALUES(54,'BJ-3',11);
INSERT INTO "variant" VALUES(55,'BJ-2',11);
INSERT INTO "variant" VALUES(56,'ST. IVES'' BLUES',12);
INSERT INTO "variant" VALUES(57,'VND-1AA',12);
INSERT INTO "variant" VALUES(58,'VND-1R',12);
INSERT INTO "variant" VALUES(59,'VND-1X',12);
INSERT INTO "variant" VALUES(60,'CN9-A',14);
INSERT INTO "variant" VALUES(61,'CN9-AL',14);
INSERT INTO "variant" VALUES(62,'CN9-D',14);
INSERT INTO "variant" VALUES(63,'CN9-AH',14);
INSERT INTO "variant" VALUES(64,'YEN-LO-WANG',14);
INSERT INTO "variant" VALUES(65,'CRB-27',18);
INSERT INTO "variant" VALUES(66,'CRB-27B',18);
INSERT INTO "variant" VALUES(67,'CRB-27SL',18);
INSERT INTO "variant" VALUES(68,'CRB-20',18);
INSERT INTO "variant" VALUES(69,'CRB-FL',18);
INSERT INTO "variant" VALUES(70,'ENF-4P',16);
INSERT INTO "variant" VALUES(71,'ENF-4R',16);
INSERT INTO "variant" VALUES(72,'ENF-5D',16);
INSERT INTO "variant" VALUES(73,'ENF-5P',16);
INSERT INTO "variant" VALUES(74,'ENF-GH',16);
INSERT INTO "variant" VALUES(75,'HBK-4G',15);
INSERT INTO "variant" VALUES(76,'GRID IRON',15);
INSERT INTO "variant" VALUES(77,'HBK-4H',15);
INSERT INTO "variant" VALUES(78,'HBK-4J',15);
INSERT INTO "variant" VALUES(79,'HBK-4P',15);
INSERT INTO "variant" VALUES(80,'HBK-4SP',15);
INSERT INTO "variant" VALUES(81,'LOUP DE GUERRE',17);
INSERT INTO "variant" VALUES(82,'TBT-3C',17);
INSERT INTO "variant" VALUES(83,'TBT-5J',17);
INSERT INTO "variant" VALUES(84,'TBT-5N',17);
INSERT INTO "variant" VALUES(85,'TBT-7K',17);
INSERT INTO "variant" VALUES(86,'TBT-7M',17);
INSERT INTO "variant" VALUES(87,'GRF-1N',21);
INSERT INTO "variant" VALUES(88,'GRF-1S',21);
INSERT INTO "variant" VALUES(89,'GRF-2N',21);
INSERT INTO "variant" VALUES(90,'GRF-3M',21);
INSERT INTO "variant" VALUES(91,'SPARKY',21);
INSERT INTO "variant" VALUES(92,'GOLDEN BOY',19);
INSERT INTO "variant" VALUES(93,'KTO-18',19);
INSERT INTO "variant" VALUES(94,'KTO-19',19);
INSERT INTO "variant" VALUES(95,'KTO-20',19);
INSERT INTO "variant" VALUES(96,'QUARANTINE',22);
INSERT INTO "variant" VALUES(97,'WVR-6K',22);
INSERT INTO "variant" VALUES(98,'WVR-6R',22);
INSERT INTO "variant" VALUES(99,'WVR-7D',22);
INSERT INTO "variant" VALUES(100,'WVR-7K',22);
INSERT INTO "variant" VALUES(101,'BSW-X1',23);
INSERT INTO "variant" VALUES(102,'BSW-X2',23);
INSERT INTO "variant" VALUES(103,'BSW-S2',23);
INSERT INTO "variant" VALUES(104,'BSW-P1',23);
INSERT INTO "variant" VALUES(105,'BSW-P2',23);
INSERT INTO "variant" VALUES(106,'BSW-HR',23);
INSERT INTO "variant" VALUES(107,'DRG-1C',24);
INSERT INTO "variant" VALUES(108,'DRG-1N',24);
INSERT INTO "variant" VALUES(109,'DRG-5N',24);
INSERT INTO "variant" VALUES(110,'FANG',24);
INSERT INTO "variant" VALUES(111,'FLAME',24);
INSERT INTO "variant" VALUES(112,'IV-FOUR',25);
INSERT INTO "variant" VALUES(113,'QKD-4G',25);
INSERT INTO "variant" VALUES(114,'QKD-4H',25);
INSERT INTO "variant" VALUES(115,'QKD-5K',25);
INSERT INTO "variant" VALUES(116,'RFL-3C',26);
INSERT INTO "variant" VALUES(117,'LEGEND-KILLER',26);
INSERT INTO "variant" VALUES(118,'RFL-3N',26);
INSERT INTO "variant" VALUES(119,'RFL-5D',26);
INSERT INTO "variant" VALUES(120,'BUTTERBEE',27);
INSERT INTO "variant" VALUES(121,'CPLT-A1',27);
INSERT INTO "variant" VALUES(122,'CPLT-C1',27);
INSERT INTO "variant" VALUES(123,'CPLT-C4',27);
INSERT INTO "variant" VALUES(124,'CPLT-K2',27);
INSERT INTO "variant" VALUES(125,'JESTER',27);
INSERT INTO "variant" VALUES(126,'FIREBRAND',28);
INSERT INTO "variant" VALUES(127,'JM6-A',28);
INSERT INTO "variant" VALUES(128,'JM6-DD',28);
INSERT INTO "variant" VALUES(129,'JM6-S',28);
INSERT INTO "variant" VALUES(130,'TDR-5S',29);
INSERT INTO "variant" VALUES(131,'TDR-9S',29);
INSERT INTO "variant" VALUES(132,'TDR-9SE',29);
INSERT INTO "variant" VALUES(133,'TOP DOG',29);
INSERT INTO "variant" VALUES(134,'TDR-5SS',29);
INSERT INTO "variant" VALUES(135,'ARC-2R',33);
INSERT INTO "variant" VALUES(136,'ARC-5S',33);
INSERT INTO "variant" VALUES(137,'ARC-5W',33);
INSERT INTO "variant" VALUES(138,'TEMPEST',33);
INSERT INTO "variant" VALUES(139,'CTF-0XP',30);
INSERT INTO "variant" VALUES(140,'CTF-1X',30);
INSERT INTO "variant" VALUES(141,'CTF-2X',30);
INSERT INTO "variant" VALUES(142,'CTF-3D',30);
INSERT INTO "variant" VALUES(143,'CTF-4X',30);
INSERT INTO "variant" VALUES(144,'ILYA MUROMETS',30);
INSERT INTO "variant" VALUES(145,'CTF-3L',30);
INSERT INTO "variant" VALUES(146,'GHR-5P',31);
INSERT INTO "variant" VALUES(147,'GHR-5H',31);
INSERT INTO "variant" VALUES(148,'GHR-5J',31);
INSERT INTO "variant" VALUES(149,'GHR-5N',31);
INSERT INTO "variant" VALUES(150,'GHR-MJ',31);
INSERT INTO "variant" VALUES(151,'BLACK WIDOW',32);
INSERT INTO "variant" VALUES(152,'WHM-6D',32);
INSERT INTO "variant" VALUES(153,'WHM-6R',32);
INSERT INTO "variant" VALUES(154,'WHM-7S',32);
INSERT INTO "variant" VALUES(155,'BOUNTY HUNTER II',36);
INSERT INTO "variant" VALUES(156,'MAD-3R',36);
INSERT INTO "variant" VALUES(157,'MAD-5D',36);
INSERT INTO "variant" VALUES(158,'MAD-5M',36);
INSERT INTO "variant" VALUES(159,'ON1-K',34);
INSERT INTO "variant" VALUES(160,'ON1-M',34);
INSERT INTO "variant" VALUES(161,'ON1-V',34);
INSERT INTO "variant" VALUES(162,'ON1-VA',34);
INSERT INTO "variant" VALUES(163,'PROTECTOR',34);
INSERT INTO "variant" VALUES(164,'AWS-8Q',37);
INSERT INTO "variant" VALUES(165,'AWS-8R',37);
INSERT INTO "variant" VALUES(166,'AWS-8T',37);
INSERT INTO "variant" VALUES(167,'AWS-8V',37);
INSERT INTO "variant" VALUES(168,'AWS-9M',37);
INSERT INTO "variant" VALUES(169,'PRETTY BABY',37);
INSERT INTO "variant" VALUES(170,'DRAGON SLAYER',38);
INSERT INTO "variant" VALUES(171,'VTR-9B',38);
INSERT INTO "variant" VALUES(172,'VTR-9K',38);
INSERT INTO "variant" VALUES(173,'VTR-9S',38);
INSERT INTO "variant" VALUES(174,'ZEU-5S',39);
INSERT INTO "variant" VALUES(175,'ZEU-6S',39);
INSERT INTO "variant" VALUES(176,'ZEU-6T',39);
INSERT INTO "variant" VALUES(177,'ZEU-9S',39);
INSERT INTO "variant" VALUES(178,'ZEU-9S2',39);
INSERT INTO "variant" VALUES(179,'ZEU-SK',39);
INSERT INTO "variant" VALUES(180,'BLR-1D',40);
INSERT INTO "variant" VALUES(181,'BLR-1G',40);
INSERT INTO "variant" VALUES(182,'BLR-1S',40);
INSERT INTO "variant" VALUES(183,'BLR-2C',40);
INSERT INTO "variant" VALUES(184,'BLR-3M',40);
INSERT INTO "variant" VALUES(185,'BLR-3S',40);
INSERT INTO "variant" VALUES(186,'HELLSLINGER',40);
INSERT INTO "variant" VALUES(187,'MISERY',41);
INSERT INTO "variant" VALUES(188,'STK-3F',41);
INSERT INTO "variant" VALUES(189,'STK-3H',41);
INSERT INTO "variant" VALUES(190,'STK-4N',41);
INSERT INTO "variant" VALUES(191,'STK-5M',41);
INSERT INTO "variant" VALUES(192,'STK-5S',41);
INSERT INTO "variant" VALUES(193,'STK-3FB',41);
INSERT INTO "variant" VALUES(194,'CP-10-Q',44);
INSERT INTO "variant" VALUES(195,'CP-10-Z',44);
INSERT INTO "variant" VALUES(196,'CP-11-A',44);
INSERT INTO "variant" VALUES(197,'CP-11-A-DC',44);
INSERT INTO "variant" VALUES(198,'CP-11-P',44);
INSERT INTO "variant" VALUES(199,'SLEIPNIR ',44);
INSERT INTO "variant" VALUES(200,'HEAVY METAL',42);
INSERT INTO "variant" VALUES(201,'HGN-732',42);
INSERT INTO "variant" VALUES(202,'HGN-732B',42);
INSERT INTO "variant" VALUES(203,'HGN-733',42);
INSERT INTO "variant" VALUES(204,'HGN-733C',42);
INSERT INTO "variant" VALUES(205,'HGN-733P',42);
INSERT INTO "variant" VALUES(206,'MAL-1P',43);
INSERT INTO "variant" VALUES(207,'MAL-1R',43);
INSERT INTO "variant" VALUES(208,'MAL-2P',43);
INSERT INTO "variant" VALUES(209,'MAL-MX90',43);
INSERT INTO "variant" VALUES(210,'MAL-KO',43);
INSERT INTO "variant" VALUES(211,'BNC-3E',45);
INSERT INTO "variant" VALUES(212,'BNC-3M',45);
INSERT INTO "variant" VALUES(213,'BNC-3S',45);
INSERT INTO "variant" VALUES(214,'LA MALINCHE',45);
INSERT INTO "variant" VALUES(215,'BOAR''S HEAD',46);
INSERT INTO "variant" VALUES(216,'AS7-D',46);
INSERT INTO "variant" VALUES(217,'AS7-D-DC',46);
INSERT INTO "variant" VALUES(218,'AS7-K',46);
INSERT INTO "variant" VALUES(219,'AS7-RS',46);
INSERT INTO "variant" VALUES(220,'AS7-S',46);


COMMIT;
