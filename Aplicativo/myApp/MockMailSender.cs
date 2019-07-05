using System;

public class MockMailSender : IMailSender
{
    public void Send(string toAddress, string subject)
    {
        Console.WriteLine("Mocking mail a [{0}] con asunto [{1}]", toAddress, subject);
    }
}