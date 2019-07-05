using System;
public class FormHandler
{
    private readonly IMailSender mailSender;

    public FormHandler(IMailSender mailSender)
    {
        this.mailSender = mailSender;
    }

    public void Handle(string toAddress)
    {
        mailSender.Send(toAddress, "Este es un ejemplo de Ninject");
    }
}