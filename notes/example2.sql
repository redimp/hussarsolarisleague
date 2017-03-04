INSERT INTO "user" VALUES(1,'Tomato','$2b$12$G9oxBVF/GMMUwmAvEiRmNuca0ITwcTIxkLLmPDlP60rbcLjSjcb8K','mail@redimp.de','2017-03-02 09:12:14.678289',0,0);

INSERT INTO "user" VALUES(2,'Potatoe','$2b$12$5ZkfQbkH2hW4PwpDu384m.Dr3dImqr8yDWT5i0PCEfUCF8bKOcXOa','potatoe@redimp.de','2017-03-01 21:33:09.919000',0,0);

DELETE FROM "game";
INSERT INTO "game" VALUES (1,1,1,2,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (2,2,2,1,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (1,3,1,2,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (2,4,2,1,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (1,5,1,2,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (2,6,2,1,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (1,7,1,2,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO "game" VALUES (2,8,2,1,0,0,NULL,NULL,NULL,NULL,NULL,NULL,1);

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
