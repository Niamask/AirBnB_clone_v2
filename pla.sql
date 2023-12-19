USE hbnb_dev_db;
CREATE TABLE places (
        id VARCHAR(60) NOT NULL, 
        created_at DATETIME NOT NULL, 
        updated_at DATETIME NOT NULL, 
        city_id varchar(60) NOT NULL, 
        user_id varchar(60) NOT NULL, 
        name VARCHAR(128) NOT NULL, 
        description VARCHAR(1024), 
        number_rooms INTEGER NOT NULL, 
        number_bathrooms INTEGER NOT NULL, 
        max_guest INTEGER NOT NULL, 
        price_by_night INTEGER NOT NULL, 
        latitude FLOAT, 
        longitude FLOAT, 
        PRIMARY KEY (id),
        CONSTRAINT `places_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`),
        CONSTRAINT `places_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
);
