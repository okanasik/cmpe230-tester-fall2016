all: Main.jar

Main.jar: Main.class
	@jar cvfe Main.jar Main Main.class

Main.class: Main.java
	@javac Main.java
	
run: Main.jar
	@java -jar Main.jar ${ARGS}
	
clean:
	@rm Main.jar *.class
