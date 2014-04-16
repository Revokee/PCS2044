package Model;

public class Pedido {

	private String nomePedido;
	private String nomeCliente;
	private String endereco;
	private String observacao;
	private String produtos;
	private String valor;
	private double latitude;
	private double longitude;
	private int ordemEntrega;
	
	public Pedido(String pedido, String cliente, String endereco, String produtos)
	{
		this.nomePedido = pedido;
		this.nomeCliente = cliente;
		this.endereco = endereco;
		this.produtos = produtos;
	}
	
	public String getNomeCliente() {
		return nomeCliente;
	}
	public void setNomeCliente(String nomeCliente) {
		this.nomeCliente = nomeCliente;
	}
	public String getProdutos() {
		return produtos;
	}
	public void setProdutos(String produtos) {
		this.produtos = produtos;
	}
	public String getEndereco() {
		return endereco;
	}
	public void setEndereco(String endereco) {
		this.endereco = endereco;
	}

	public String getObservacao() {
		return observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getNomePedido() {
		return nomePedido;
	}

	public void setNomePedido(String nomePedido) {
		this.nomePedido = nomePedido;
	}

	public String getValor() {
		return valor;
	}

	public void setValor(String valor) {
		this.valor = valor;
	}

	public double getLongitude() {
		return longitude;
	}

	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}

	public double getLatitude() {
		return latitude;
	}

	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}

	public int getOrdemEntrega() {
		return ordemEntrega;
	}

	public void setOrdemEntrega(int ordemEntrega) {
		this.ordemEntrega = ordemEntrega;
	}
	
	
	
	
}
