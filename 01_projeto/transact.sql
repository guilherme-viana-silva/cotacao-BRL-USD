-- Criar o database (se não existir)
IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = N'finanças'
)
BEGIN
    CREATE DATABASE [finanças];
END
GO

-- Usar o database
USE [finanças];
GO

-- Criar a tabela (se não existir)
IF NOT EXISTS (
    SELECT * 
    FROM sys.objects 
    WHERE object_id = OBJECT_ID(N'dbo.cotacao_real') 
    AND type = 'U'
)
BEGIN
    CREATE TABLE dbo.cotacao_real (
        id INT IDENTITY(1,1) PRIMARY KEY,
        moeda VARCHAR(5) NOT NULL,
        cotacao DECIMAL(10,4) NOT NULL,
        data DATE NOT NULL,
        moeda_base VARCHAR(5) NOT NULL,
        CONSTRAINT UC_Moeda_Data UNIQUE (moeda, data)
    );
END
GO

