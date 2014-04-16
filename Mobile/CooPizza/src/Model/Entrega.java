package Model;

import java.io.Serializable;
import java.util.ArrayList;

public class Entrega implements Serializable {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String nome;
	private int numeroDePedidos;
	
	public ArrayList<Pedido> listaPedidos = new ArrayList<Pedido>();

	public Entrega(String nome)
	{
		this.nome = nome;
	}


	public int getNumeroPedidos() {
		return numeroDePedidos;
	}

	public void setNumeroPedidos(int numeroPedidos) {
		this.numeroDePedidos = numeroPedidos;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
	

	
	
}
