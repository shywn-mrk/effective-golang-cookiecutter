package grpc_server

import (
    "log"
    "net"

    "google.golang.org/grpc"
    // pb "{{ cookiecutter.project_complete_name }}/your/module/path/proto" // Replace with your actual import path
)

func StartGRPCServer() {
    lis, err := net.Listen("tcp", ":50051")
    if err != nil {
        log.Fatalf("failed to listen: %v", err)
    }
    s := grpc.NewServer()
    // pb.RegisterYourServiceServer(s, &pb.UnimplementedYourServiceServer{}) // Replace with your actual service

    log.Println("gRPC server listening on :50051")
    if err := s.Serve(lis); err != nil {
        log.Fatalf("failed to serve: %v", err)
    }
}
