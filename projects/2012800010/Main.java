import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;

public class Main {

	protected static void processStatements(List<String> inputLines, String outputFileName) {
		try {
			int value = 0;
			char variable = '0';
			BufferedWriter bw = new BufferedWriter(new FileWriter(outputFileName));
			bw.write("jmp start\n");
			for (String line : inputLines) {
				if (line.indexOf("=") >= 0) {
					variable = line.charAt(0);
					value = line.charAt(2);
					bw.write(variable + " db " + value + "\n");
				} else if (line.charAt(0) == variable) {
					bw.write("start:\n");
					bw.write("  mov ah,02\n");
					bw.write("  mov dl,"+variable+"\n");
					bw.write("  int 21h\n");
				}
			}
			bw.write("exit:\n");
			bw.write("  mov ah,4ch\n");
			bw.write("  mov al,00\n");
			bw.write("  int 21h\n");
			bw.close();
		} catch (IOException ex) {
			System.out.println(ex.getMessage());
		}
		
	}
	
	protected static void runInterpreter() {
		int value = 0;
		char variable = '0';
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String line = br.readLine();
			while(line != null) {
				if (line.indexOf("=") >= 0) {
					variable = line.charAt(0);
					value = line.charAt(2)-'0';
				} else if (line.charAt(0) == variable) {
					System.out.println(value);
				}
				line = br.readLine();
			}
		} catch (IOException ex) {
			System.out.println(ex.getMessage());
		}
	}
	
	protected static void runCompiler(String inputFile) {
		List<String> inputLines = new ArrayList<String>();
		try {
			BufferedReader br = new BufferedReader(new FileReader(inputFile));
			String line = br.readLine();
			while(line != null) {
				inputLines.add(line);
				line = br.readLine();
			}
		} catch (IOException ex) {
			System.out.println(ex.getMessage());
		}
		// if input file has ".ac" extension replace this with ".asm"
		String outputFileName = inputFile + ".asm";
		processStatements(inputLines, outputFileName);
	}
	
	public static void main(String[] args) {
		if (args.length == 0) {
			// interpreter mode
			runInterpreter();
		} else if (args.length == 1) {
			// compiler mode
			runCompiler(args[0]);
		}
	}
}
