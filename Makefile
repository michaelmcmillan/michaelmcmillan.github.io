PWD=$(shell pwd)
EDITOR=$(shell which vi)
PYTHON=$(shell which python3)
POSTS=$(shell find $(POSTS_DIR) -type f -name '*')
PYTHON_FLAGS=-B
LIB_DIR=lib/
POSTS_DIR=posts/
TEMPLATE_DIR=templates/
TEST_DIR=test/
INDEX=index.html
FEED=feed.rss
MODULES=$(PWD)/$(LIB_DIR)
EDITOR_CONFIG=$(LIB_DIR)/vim.rc
COMPILER=$(LIB_DIR)/build.py
XML_TEMPLATES=$(shell find $(TEMPLATE_DIR) -type f -name '*.xml')
HTML_TEMPLATES=$(shell find $(TEMPLATE_DIR) -type f -name '*.html')
PYTHON_TEST_FLAGS=-m unittest discover -p '*_test.py' -s $(TEST_DIR)

all: $(INDEX) $(FEED)

$(INDEX): $(COMPILER) $(HTML_TEMPLATES) $(POSTS)
	$(PYTHON) $(PYTHON_FLAGS) $(COMPILER) blog $(POSTS_DIR) $(TEMPLATE_DIR) > $(INDEX)

$(FEED): $(COMPILER) $(XML_TEMPLATES) $(POSTS)
	$(PYTHON) $(PYTHON_FLAGS) $(COMPILER) feed $(POSTS_DIR) $(TEMPLATE_DIR) > $(FEED)

post:
	$(EDITOR) $(POSTS_DIR)/draft-`date +%Y-%m-%d`-title.txt -u $(EDITOR_CONFIG)

test: export PYTHONPATH=$(MODULES)
test:
	$(PYTHON) $(PYTHON_FLAGS) $(PYTHON_TEST_FLAGS)

.PHONY: post test
