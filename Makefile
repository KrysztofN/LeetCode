leet:
	git add .
	git commit -m "leet $(word 2,$(MAKECMDGOALS)) added"
	git push -u origin main

%:
	@: