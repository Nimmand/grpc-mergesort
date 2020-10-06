using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Grpc.Core;
using Microsoft.Extensions.Logging;

namespace RNGesus
{
    public class RngesusService : Rngesus.RngesusBase
    {
        private readonly ILogger<RngesusService> _logger;
        public RngesusService(ILogger<RngesusService> logger)
        {
            _logger = logger;
        }

        public override Task<RngReply> GenerateNumbers(RngRequest request, ServerCallContext context)
        {
            System.Console.WriteLine($"Called with Count = {request.RngCount}, Max = {request.RngMax}");
            Random rnd = new Random();
            var reply = new RngReply();
            for(int i = 0; i < request.RngCount; i++){
                reply.Numbers.Add(rnd.Next(1, request.RngMax));
            }
            return Task.FromResult(reply);
        }
    }
}
