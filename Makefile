COMPILER=build.py
POSTS_DIR=posts/
TEMPLATE_DIR=templates/
PYTHON=$(shell which python3)
POSTS=$(shell find $(POSTS_DIR) -type f -name '*')
TEMPLATES=$(shell find $(TEMPLATE_DIR) -type f -name '*')

index.html: $(COMPILER) $(TEMPLATES) $(POSTS)
	$(PYTHON) $(COMPILER) $(POSTS_DIR) $(TEMPLATE_DIR) > index.html
