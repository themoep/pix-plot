
.PHONY: model
model:
	pixplot --images "testicons/*" --metadata "metadata.csv"
	

show: output
	exo-open http://localhost:5000/output
	python -m http.server 5000 2>&1 > /dev/null
	

.PHONY: clean
clean:
	trash output
