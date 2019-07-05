using System;
public class MailSender : IMailSender
{
    public void Send(string toAddress, string subject)
    {
      Console.WriteLine("Enviando mail a [{0}] con asunto [{1}]", toAddress, subject);
    }
}