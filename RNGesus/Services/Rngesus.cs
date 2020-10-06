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
            Random rnd = new Random();
            var reply = new RngReply();
            for(int i = 0; i < request.Count; i++){
                reply.Numbers.Add(rnd.Next(1, request.Max));
            }
            return Task.FromResult(reply);
        }
    }
}
