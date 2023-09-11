from xml.etree import ElementTree
import json

class Movie:
    def __init__(self,
                 title,
                 format,
                 year,
                 rating,
                 description,
                 category):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category


    @classmethod
    def from_xml(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for genre in collection:
            for decade in genre:
                for movie in decade:
                    movies.append(cls(
                        movie.attrib['title'],
                        movie.find('format').text,
                        movie.find('year').text,
                        movie.find('rating').text,
                        movie.find('description').text,
                        genre.attrib['category']
                    ))
        return movies

    def to_xml_string(self):
        movie_element = ElementTree.Element("movie", title=self.title)
        ElementTree.SubElement(movie_element, "format").text = self.format
        ElementTree.SubElement(movie_element, "year").text = self.year
        ElementTree.SubElement(movie_element, "rating").text = self.rating
        ElementTree.SubElement(movie_element, "description").text = self.description
        return ElementTree.tostring(movie_element).decode()

    @classmethod
    def from_xml_string(cls, xml_string):
        root = ElementTree.fromstring(xml_string)
        title = root.attrib['title']
        format = root.find('format').text
        year = root.find('year').text
        rating = root.find('rating').text
        description = root.find('description').text
        category = None
        return cls(title, format, year, rating, description, category)

    @classmethod
    def save_to_json(cls, movies, file_path):
        with open(file_path, 'w') as json_file:
            for movie in movies:
                movie_dict = {
                    'title': movie.title,
                    'format': movie.format,
                    'year': movie.year,
                    'rating': movie.rating,
                    'description': movie.description,
                    'category': movie.category
                }
                json.dump(movie_dict, json_file)
                json_file.write('\n')

movies = Movie.from_xml("films.xml")
for movie in movies:
    print(movie.title)

movie = movies[1]
xml_str = movie.to_xml_string()
print(xml_str)
decoded_movie = Movie.from_xml_string(xml_str)
print(decoded_movie.title)

movie.save_to_json(movies, "films.json")
print("JSON created")

