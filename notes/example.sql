INSERT INTO "hangar" VALUES(1,1,10,1,0,0);
INSERT INTO "hangar" VALUES(2,1,13,1,0,0);
INSERT INTO "hangar" VALUES(3,1,17,1,0,0);
INSERT INTO "hangar" VALUES(4,1,29,1,0,0);
INSERT INTO "hangar" VALUES(5,1,31,1,0,0);
INSERT INTO "hangar" VALUES(6,1,33,1,0,0);
INSERT INTO "hangar" VALUES(7,1,40,1,0,0);
INSERT INTO "hangar" VALUES(8,1,41,1,0,0);
INSERT INTO "hangar" VALUES(9,1,42,1,0,0);
INSERT INTO "hangar" VALUES(10,1,3,1,0,1);

INSERT INTO "hangar" VALUES(11,2,10,1,0,0);
INSERT INTO "hangar" VALUES(12,2,13,1,0,0);
INSERT INTO "hangar" VALUES(13,2,17,1,0,0);
INSERT INTO "hangar" VALUES(14,2,29,1,0,0);
INSERT INTO "hangar" VALUES(15,2,31,1,0,0);
INSERT INTO "hangar" VALUES(16,2,33,1,0,0);
INSERT INTO "hangar" VALUES(17,2,40,1,0,0);
INSERT INTO "hangar" VALUES(18,2,41,1,0,0);
INSERT INTO "hangar" VALUES(19,2,42,1,0,0);
INSERT INTO "hangar" VALUES(20,2,3,1,0,1);

INSERT INTO "user" VALUES(1,'Red Imp','$2b$12$G9oxBVF/GMMUwmAvEiRmNuca0ITwcTIxkLLmPDlP60rbcLjSjcb8K','mail@redimp.de','2017-03-02 09:12:14.678289',0,0);

INSERT INTO "user" VALUES(2,'Potatoe','$2b$12$5ZkfQbkH2hW4PwpDu384m.Dr3dImqr8yDWT5i0PCEfUCF8bKOcXOa','potatoe@redimp.de','2017-03-01 21:33:09.919000',0,0);

DELETE FROM "game";
INSERT INTO "game" VALUES (1,1,1,2,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (2,2,2,1,0,0,NULL,NULL,NULL,NULL,NULL,NULL,0);

--    id = db.Column('id', db.Integer, primary_key=True)
--    day = db.Column('day', db.Integer)
--    player_home_id = db.Column('player_home', db.Integer, db.ForeignKey('user.id'))
--    player_away_id = db.Column('player_away', db.Integer, db.ForeignKey('user.id'))
--    ready_home = db.Column('ready_home', db.Boolean)
--    ready_away = db.Column('ready_away', db.Boolean)
--    winner = db.Column('winner', db.Integer, db.ForeignKey('user.id'), nullable=True)
--    mech_home = db.Column('mech_home', db.Integer, db.ForeignKey('hangar.id'), nullable=True)
--    mech_away = db.Column('mech_away', db.Integer, db.ForeignKey('hangar.id'), nullable=True)
--    map = db.Column('map', db.Enum(*Maps), nullable=True)
--    status = db.Column('status', db.Integer, nullable=False, default=0)
