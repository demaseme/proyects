init: 
	python3 -m pip install -r requirements.txt 
handler_package:
	python3 -m pip install --target ./target . --upgrade
	cd target \
	&& zip -FSr ../../orders.zip . \
	&& cd ..\
	&& rm -rf target 