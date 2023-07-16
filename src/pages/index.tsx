import React from 'react';
import axios from 'axios';
import { GetServerSideProps, InferGetServerSidePropsType } from 'next';

export const getServerSideProps: GetServerSideProps<{
  time: string;
}> = async () => {
  const res = await axios.get(process.env.API_URL + '/time', {
    responseType: 'json',
    headers: { 'Content-Type': 'application/json' }
  });
  console.log('~~ !res ', res);
  return { props: { time: res.data?.time } };
};

const Home = ({ time }: InferGetServerSidePropsType<typeof getServerSideProps>) => {
  return (
    <>
      <h1 className="text-3xl font-bold underline">{time}</h1>
    </>
  );
};

export default Home;
