#! /usr/bin/ruby -w

#Autora: María Angélica Serrano Mora
#Estudiante UIS : 2171985

let = ('A'..'Z') #abecedario generado por Ruby 
@alfabeto=let.to_a #Convertido en array
@alfabeto.insert(14,'Ñ') #Se inserta la letra Ñ que no existe en el abecedario inglés


def encrypt_menu #Menu de cifrar y seleccionar metodos
	puts "------------------------------"
	puts "Welcome to the Encrypt menu"
	puts "------------------------------"
	puts "Select a method"   
	puts "------------------------------"
	puts "1. Desplazamiento - Cesar"
	puts "2. Sustitución Afín"
	puts "------------------------------"

	case gets.strip
		when "1"
		puts"Ingrese el mensaje a cifrar"
		mensaje = $stdin.gets.chomp
		mensaje_m = mensaje.upcase
		puts "Ingrese el numero de saltos para cifrar"
		saltos = $stdin.gets.chomp
		cesar( mensaje_m, saltos.to_i) 
		when "2"
		puts"Ingrese el mensaje a cifrar"
		mensaje = $stdin.gets.chomp
		mensaje.upcase
		sustitucion_af( mensaje )
	end
end

def cesar( mensaje_m, saltos )	
	cifrado = ""
	
	mensaje_m.each_char do |letter|
		if letter == " "
			cifrado += " "
		else
			old_inx = @alfabeto.find_index(letter)
			new_inx = ( old_inx + saltos ).modulo(@alfabeto.count)
			cifrado += @alfabeto[new_inx]
		end
	end
	puts "El mensaje descifrado es: #{cifrado}"
end

def sustitucion_af( mensaje )

	abc_coun = []

	for i in 0..26 do
		abc_coun.append(mensaje.count(@alfabeto[i]))
	end

	@ordenado =  abc_coun.sort{ |a, b|
		if a >= b
			-1
		elsif
		a <= b
			1
		else
			0
		end
	}


	def solucion(a)

		for x in 0..26
			if @ordenado[0] == a[x]
				@primero = x
			end
	
			if @ordenado[1] == a[x]
				@segundo = x
			end
	
		end
	end
	
	solucion(abc_coun)
	puts "letra mas repetida: #{@primero} segunda: #{@segundo}" 


	@b = @primero % 27
	@a = (((@segundo - @b) * 7) % 27).abs

	cifrado = ""
	
	mensaje.each_char do |letter|
		if letter == " "
			cifrado += " "
		else
			old_inx = @alfabeto.find_index(letter)
			new_inx = ( @a * old_inx + @b ).modulo(@alfabeto.count)
			cifrado += @alfabeto[new_inx]
		end
	end
	puts "El mensaje descifrado es: #{cifrado}"

end

def decrypt_menu #Menu de descifrar y seleccionar metodos
	puts "-----------------------------"
	puts "Welcome to the Decrypt menu"
	puts "-----------------------------"
	puts "Select a method"
	puts "-----------------------------"
	puts "1. Desplazamiento - Cesar"
	puts "2. Sustitución Afín"
	puts "-----------------------------"

	case gets.strip
		when "1"
		# puts"Ingrese el mensaje a descifrar"
		# mensaje = $stdin.gets.chomp
		# mensaje_m = mensaje.upcase
		# puts "Ingrese el numero de saltos para decifrar"
		# saltos = $stdin.gets.chomp
		mensaje_m = 'PYWAE AUAEO PWUAH PYMDO PWMWW MXMPY WAEOP WHTPU ANDTW WMWMW GLHTÑ FADSG RA'
		cesar_de( mensaje_m, 12 )
		when "2"
		# puts"Ingrese el mensaje a descifrar"
		# mensaje = $stdin.gets.chomp
		# mensaje_m = mensaje.to_s
		string = "JFWFG DSWHM HWOCA FRPQG DGWSC AGWGO KGOHK GOGWW FYCOO HZGÑF WZGKG OGWBF MFDKF SCOSC OKFWB CPQGD HGOKG GBFBI FCQOF AHDKC WHFNF OKFDK HSFPQ GZGBG HKGDQ GVCDF ÑGOCD CKFBX GYSWG GWBCP QGOQO SFNQG."
		sustitucion_af_de( string )
	end
end

def cesar_de( cesar, saltos )
	cesar( cesar, saltos * -1 )
end

def sustitucion_af_de( mensaje )

	abc_coun = []

	for i in 0..26 do
		abc_coun.append(mensaje.count(@alfabeto[i]))
	end

	@ordenado =  abc_coun.sort{ |a, b|
		if a >= b
			-1
		elsif
		a <= b
			1
		else
			0
		end
	}


	def solucion(a)

		for x in 0..26
			if @ordenado[0] == a[x]
				@primero = x
			end
	
			if @ordenado[1] == a[x]
				@segundo = x
			end
	
		end
	end
	
	solucion(abc_coun)
	puts "letra mas repetida: #{@primero} segunda: #{@segundo}" 


	@b = @primero % 27
	@a = (((@segundo - @b) * 7) % 27).abs

	cifrado = ""
	
	for bb in 1..27 do

		aa = (((@segundo - bb) * 7) % 27).abs
		cifrado = ""

        k1_re = 1
        if(aa.gcd(27)==1)
            for i in 0..26 do
                if((aa*i)%27==1)
                    k1_re=i
                    break
                end
            end
        end

        mensaje.each_char do |letter|
            if letter == " "
                cifrado += " "
            else
                old_inx = @alfabeto.find_index(letter)
                new_inx = (((old_inx - bb + 27).abs * k1_re)) % 27
                cifrado += @alfabeto[new_inx]
            end
        end
        puts "El mensaje descifrado es: #{cifrado} \n"

    end


end


def menu #Menu para seleccionar la opción de cifrar o descifrar

	puts "------------------------------"
	puts "Welcome to the Crypto menu"
	puts "------------------------------"
	puts "Select an option"
	puts "------------------------------"
	puts "1. Encrypt"
	puts "2. Decrypt"
	puts "------------------------------"
	case gets.strip
		when "1"
		encrypt_menu
		when "2"
		decrypt_menu
	end
end
menu
