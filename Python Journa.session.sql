CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `date` TEXT NOT NULL,
    `mood_id` INTEGER,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
)

CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
)

INSERT INTO `Entry` VALUES (null, 'SQL', "I learned about SQL today in class. Was pretty good", "2021-03-06", "3");
INSERT INTO `Entry` VALUES (null, 'React', "I learned about React today in class. Was pretty bad", "2021-03-07", "4");

INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Morose");
INSERT INTO `Mood` VALUES (null, "Unwell");
INSERT INTO `Mood` VALUES (null, "Frustrated");

SELECT id, concept, `entry`, `date`, mood_id
FROM `Entry`
WHERE `entry` LIKE "%React%";

SELECT id, label
FROM Mood

SELECT
    e.id,
    e.concept,
    e.entry,
    e.date,
    e.mood_id,
    m.label mood_label
FROM entry e
JOIN Mood m
    ON m.id = e.mood_id 


