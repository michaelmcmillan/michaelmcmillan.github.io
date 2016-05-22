PYTHON=$(shell which python3)
POSTS=$(shell find $(POSTS_DIR) -type f -name '*')
LIB_DIR=lib/
POSTS_DIR=posts/
TEMPLATE_DIR=templates/
INDEX=index.html
FEED=feed.rss
COMPILER=$(LIB_DIR)/build.py
XML_TEMPLATES=$(shell find $(TEMPLATE_DIR) -type f -name '*.xml')
HTML_TEMPLATES=$(shell find $(TEMPLATE_DIR) -type f -name '*.html')

all: $(INDEX) $(FEED)

$(INDEX): $(COMPILER) $(HTML_TEMPLATES) $(POSTS)
	$(PYTHON) $(COMPILER) blog $(POSTS_DIR) $(TEMPLATE_DIR) > $(INDEX)

$(FEED): $(COMPILER) $(XML_TEMPLATES) $(POSTS)
	$(PYTHON) $(COMPILER) feed $(POSTS_DIR) $(TEMPLATE_DIR) > $(FEED)
