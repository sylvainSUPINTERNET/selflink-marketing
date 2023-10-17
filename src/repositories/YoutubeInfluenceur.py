import os
from typing import List
from neo4j import GraphDatabase

from logger.logger import logging

class YoutubeInfluenceur:
    def __init__(self):
        print()
        self.driver = GraphDatabase.driver(os.getenv('NEO4J_URI'), auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASSWORD')))
        
    def close(self):
        self.driver.close()
    
    def insert_influenceur(self, name:str):
        try:
            with self.driver.session() as session:
                session.execute_write(self._insert_influenceur, f"{name}")
        except Exception as e:
            logging.info(e)
            
    def insert_category(self, category_list:List[str]):
        try:
            with self.driver.session() as session:
                session.execute_write(self._insert_category, category_list)
        except Exception as e:
            logging.info(e)
            
    def insert_subcategory(self, subcategory_list:List[str]):
        try:
            with self.driver.session() as session:
                session.execute_write(self._insert_subcategory, subcategory_list)
        except Exception as e:
            logging.info(e)
                            
    def build_tree_add_node_category(self):
        try:
            with self.driver.session() as session:
                session.execute_write(self._tree_add_node_category)
        except Exception as e:
            logging.info(e)
            
    def build_tree_add_node_subcategory(self):
        try:
            with self.driver.session() as session:
                session.execute_write(self._tree_add_node_subcategory)
        except Exception as e:
            logging.info(e)
    
    def build_tree_link_category_influenceur(self, influenceur, category):
        try:
            with self.driver.session() as session:
                session.execute_write(self._tree_add_relation_category_influenceur, influenceur, category)
        except Exception as e:
            logging.info(e)
            
    @staticmethod
    def _tree_add_relation_category_influenceur(tx, influenceur, category):
        tx.run("""
        MATCH (a:Influenceur),(b:Category)
        WHERE a.name = $name AND b.name = $category
        MERGE (a)-[r:IS_CATEGORY]->(b)
        """, name=influenceur, category=category)
    
    @staticmethod
    def _tree_add_node_category(tx):
        tx.run('CREATE CONSTRAINT FOR (a:Category) REQUIRE a.name IS UNIQUE')
        
    @staticmethod
    def _tree_add_node_subcategory(tx):
        tx.run('CREATE CONSTRAINT FOR (a:SubCategory) REQUIRE a.name IS UNIQUE')

    @staticmethod
    def _insert_influenceur(tx, influenceur):
        tx.run("MERGE (a:Influenceur {name: $name})", name=influenceur)
        
    @staticmethod
    def _insert_category(tx, category_list):
        query="""
        UNWIND $category_list AS category
        MERGE (a:Category {name: category})
        """
        tx.run(query, category_list=category_list)
        
    @staticmethod
    def _insert_subcategory(tx, subcategory_list):
        query="""
        UNWIND $subcategory_list AS subcategory
        MERGE (a:SubCategory {name: subcategory})
        """
        tx.run(query, subcategory_list=subcategory_list)
        