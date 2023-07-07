build_src:
	cd src \
	&& make handler_package
deploy_lambda:
	cd infra/funs \
	&& serverless deploy
build_and_deploy: 
	make build_src \
	&& make deploy_lambda
	